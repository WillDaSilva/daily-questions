from datetime import date, timedelta
from dateutil.parser import parse

def working_days(year, weekend=(5, 6), holidays=tuple()):
    year_start, year_end = date(year, 1, 1), date(year, 12, 31)
    year_range = range((year_end - year_start).days + 1)
    year_dates = (year_start + timedelta(x) for x in year_range)
    yield from (x for x in year_dates if not (
        x.weekday() in weekend or x in [parse(h).date() for h in holidays]))

