from formulas import time_formulas as timef
from typing import Union

unit_list = [
    "millisecond",
    "second",
    "minute",
    "hour",
    "day",
    "week",
    "month",
    "year",
    "decade",
    "century"
]


def time_converter(time: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
  if from_unit not in unit_list or to_unit not in unit_list:  
    raise ValueError("The measurement has an unknown unit")
  else:
    if from_unit == 'millisecond':
      return timef.Millisecond(time, with_unit=with_unit).millisecond_to(to_unit)
    elif from_unit == 'second':
      return timef.Second(time, with_unit=with_unit).second_to(to_unit)
    elif from_unit == 'minute':
      return timef.Minute(time, with_unit=with_unit).minute_to(to_unit)
    elif from_unit == 'hour':
      return timef.Hour(time, with_unit=with_unit).hour_to(to_unit)
    elif from_unit == 'day':
      return timef.Day(time, with_unit=with_unit).day_to(to_unit)
    elif from_unit == 'week':
      return timef.Week(time, with_unit=with_unit).week_to(to_unit)
    elif from_unit == 'month':
      return timef.Month(time, with_unit=with_unit).month_to(to_unit)
    elif from_unit == 'year':
      return timef.Year(time, with_unit=with_unit).year_to(to_unit)
    elif from_unit == 'decade':
      return timef.Decade(time, with_unit=with_unit).decade_to(to_unit)
    elif from_unit == 'century':
      return timef.Century(time, with_unit=with_unit).century_to(to_unit)
    else:
      raise ValueError("The measurement has an unknown unit")
    