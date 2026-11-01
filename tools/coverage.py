"""Screen supplied station-day coverage against a fixed three-year criterion."""
import datetime,calendar

def assess(dates,start_year,years=3,min_fraction=0.9,max_gap=7):
    if years<3 or not 0<=min_fraction<=1 or max_gap<0:raise ValueError('invalid preregistered criterion')
    start=datetime.date(start_year,1,1);end=datetime.date(start_year+years,1,1);days={datetime.date.fromisoformat(d) for d in dates};total=(end-start).days
    seen=0;gap=0;longest=0
    for offset in range(total):
        d=start+datetime.timedelta(days=offset)
        if d in days:seen+=1;gap=0
        else:gap+=1;longest=max(longest,gap)
    fraction=seen/total
    return dict(start=str(start),end_exclusive=str(end),days_expected=total,days_present=seen,fraction=fraction,longest_missing_run=longest,eligible=fraction>=min_fraction and longest<=max_gap,min_fraction=min_fraction,max_gap=max_gap)
