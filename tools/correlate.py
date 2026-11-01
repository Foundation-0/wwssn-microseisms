"""Pearson association on finite paired daily measurements; no trend inference."""
import math

class CorrelationError(ValueError):
    """A ValueError that carries the exclusion log built before the failure."""
    def __init__(self,message,exclusion_log):
        super().__init__(message);self.exclusion_log=exclusion_log

def _number(v):
    """Float value, or NaN for a missing (None/empty) or unparseable value, so it is logged rather than raised."""
    if v is None or (isinstance(v,str) and not v.strip()):return math.nan
    try:return float(v)
    except (TypeError,ValueError):return math.nan

def correlate(amplitudes,swell):
    dup=[]
    for series,rows in (('amplitude',amplitudes),('swell',swell)):
        seen=set()
        for r in rows:
            if r['date'] in seen:dup.append(dict(date=r['date'],series=series,reason='duplicate day'))
            seen.add(r['date'])
    if dup:raise CorrelationError('duplicate day',dup)
    b={r['date']:_number(r['swell']) for r in swell};amp_dates={r['date'] for r in amplitudes};exclusion=[]
    for d in sorted(set(b)-amp_dates):
        exclusion.append(dict(date=d,series='swell',reason='no amplitude for day'))
    pairs=[]
    for r in sorted(amplitudes,key=lambda x:x['date']):
        x=_number(r['amplitude']);y=b.get(r['date'])
        if y is None:
            exclusion.append(dict(date=r['date'],series='amplitude',reason='no swell for day'));continue
        if not math.isfinite(x):
            exclusion.append(dict(date=r['date'],series='amplitude',reason='non-finite amplitude'));continue
        if not math.isfinite(y):
            exclusion.append(dict(date=r['date'],series='swell',reason='non-finite swell'));continue
        pairs.append((r['date'],x,y))
    if len(pairs)<3:raise CorrelationError('at least three paired days required',exclusion)
    xs=[r[1] for r in pairs];ys=[r[2] for r in pairs];mx=sum(xs)/len(xs);my=sum(ys)/len(ys)
    vx=sum((x-mx)**2 for x in xs);vy=sum((y-my)**2 for y in ys)
    if vx==0 or vy==0:raise CorrelationError('constant series has undefined correlation',exclusion)
    r=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(vx*vy)
    return dict(n=len(pairs),pearson_r=max(-1,min(1,r)),dates=[p[0] for p in pairs],exclusion_log=exclusion)
