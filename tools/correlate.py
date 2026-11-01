"""Pearson association on finite paired daily measurements; no trend inference."""
import math

def correlate(amplitudes,swell):
    if len({r['date'] for r in amplitudes})!=len(amplitudes) or len({r['date'] for r in swell})!=len(swell):raise ValueError('duplicate day')
    b={r['date']:float(r['swell']) for r in swell};amp_dates={r['date'] for r in amplitudes};exclusion=[]
    for d in sorted(set(b)-amp_dates):
        exclusion.append(dict(date=d,series='swell',reason='no amplitude for day'))
    pairs=[]
    for r in sorted(amplitudes,key=lambda x:x['date']):
        x=float(r['amplitude']);y=b.get(r['date'])
        if y is None:
            exclusion.append(dict(date=r['date'],series='amplitude',reason='no swell for day'));continue
        if not math.isfinite(x):
            exclusion.append(dict(date=r['date'],series='amplitude',reason='non-finite amplitude'));continue
        if not math.isfinite(y):
            exclusion.append(dict(date=r['date'],series='swell',reason='non-finite swell'));continue
        pairs.append((r['date'],x,y))
    if len(pairs)<3:raise ValueError('at least three paired days required')
    xs=[r[1] for r in pairs];ys=[r[2] for r in pairs];mx=sum(xs)/len(xs);my=sum(ys)/len(ys)
    vx=sum((x-mx)**2 for x in xs);vy=sum((y-my)**2 for y in ys)
    if vx==0 or vy==0:raise ValueError('constant series has undefined correlation')
    r=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(vx*vy)
    return dict(n=len(pairs),pearson_r=max(-1,min(1,r)),dates=[p[0] for p in pairs],exclusion_log=exclusion)
