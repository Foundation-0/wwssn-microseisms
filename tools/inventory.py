"""Aggregate a normalized archive metadata CSV, retaining unique scan IDs and station-days."""
import argparse,csv,datetime,json
from collections import defaultdict

def inventory(rows):
    scans={};days=defaultdict(set);counts=defaultdict(int)
    for r in rows:
        day=datetime.date.fromisoformat(r['date']);station=r['station'].strip();sid=r['scan_id'].strip()
        if not station or not sid:raise ValueError('station and scan ID required')
        value=(station,day)
        if sid in scans:
            if scans[sid]!=value:raise ValueError('scan ID has inconsistent station/date')
            continue
        scans[sid]=value;k=(station,day.strftime('%Y-%m'));counts[k]+=1;days[k].add(day)
    return [dict(station=s,month=m,scan_count=counts[(s,m)],days_with_records=len(days[(s,m)])) for s,m in sorted(days)]
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('listing');p.add_argument('output');a=p.parse_args()
    with open(a.listing) as f:out=inventory(csv.DictReader(f))
    with open(a.output,'w') as f:json.dump(out,f,indent=2)
