"""Aggregate a normalized archive metadata CSV, retaining unique scan IDs and station-days."""
import argparse,csv,datetime,json
from collections import defaultdict

REQUIRED_FIELDS=('date','station','scan_id')

def inventory(rows):
    scans={};days=defaultdict(set);counts=defaultdict(int);quarantine=[]
    for row_num,r in enumerate(rows,start=1):
        if not isinstance(r,dict):
            quarantine.append(dict(row=row_num,reason='row not a mapping',fields=r));continue
        missing=[k for k in REQUIRED_FIELDS if k not in r]
        if missing:
            quarantine.append(dict(row=row_num,reason='missing field: '+', '.join(missing),fields={k:r.get(k) for k in r}));continue
        raw_date=r['date']
        try:
            day=datetime.date.fromisoformat(str(raw_date).strip())
        except (ValueError,AttributeError,TypeError):
            quarantine.append(dict(row=row_num,reason='invalid date: '+repr(raw_date),fields={k:r[k] for k in REQUIRED_FIELDS}));continue
        station=r['station'].strip();sid=r['scan_id'].strip()
        if not station or not sid:
            quarantine.append(dict(row=row_num,reason='empty station or scan_id',fields={k:r[k] for k in REQUIRED_FIELDS}));continue
        value=(station,day)
        if sid in scans:
            if scans[sid]!=value:raise ValueError('scan ID has inconsistent station/date')
            continue
        scans[sid]=value;k=(station,day.strftime('%Y-%m'));counts[k]+=1;days[k].add(day)
    out=[dict(station=s,month=m,scan_count=counts[(s,m)],days_with_records=len(days[(s,m)])) for s,m in sorted(days)]
    return out,quarantine
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('listing');p.add_argument('output');a=p.parse_args()
    with open(a.listing,encoding='utf-8-sig',newline='') as f:rows,quarantine=inventory(csv.DictReader(f))
    with open(a.output,'w') as f:json.dump(dict(station_months=rows,quarantine=quarantine),f,indent=2)
