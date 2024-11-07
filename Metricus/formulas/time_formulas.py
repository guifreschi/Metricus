from typing import Union

# Millisecond 
class Millisecond:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def millisecond_to(self, unit: str) -> Union[float, str]:
        if unit == 'second':
            result = self.num / 1000
        elif unit == 'minute':
            result = self.num / 60000
        elif unit == 'hour':
            result = self.num / 3.6e6
        elif unit == 'day':
            result = self.num / 8.64e7
        elif unit == 'week':
            result = self.num / 6.048e8
        elif unit == 'month':
            result = self.num / 2.628e9  
        elif unit == 'year':
            result = self.num / 3.1536e10
        elif unit == 'decade':
            result = self.num / 3.1536e11
        elif unit == 'century':
            result = self.num / 3.1536e12
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result

# Second
class Second:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def second_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 1000
        elif unit == 'minute':
            result = self.num / 60
        elif unit == 'hour':
            result = self.num / 3600
        elif unit == 'day':
            result = self.num / 86400
        elif unit == 'week':
            result = self.num / 604800
        elif unit == 'month':
            result = self.num / 2.628e6
        elif unit == 'year':
            result = self.num / 3.154e7
        elif unit == 'decade':
            result = self.num / 3.154e8
        elif unit == 'century':
            result = self.num / 3.154e9
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result

# Minute
class Minute:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def minute_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 60000
        elif unit == 'second':
            result = self.num * 60
        elif unit == 'hour':
            result = self.num / 60
        elif unit == 'day':
            result = self.num / 1440
        elif unit == 'week':
            result = self.num / 10080
        elif unit == 'month':
            result = self.num / 43800
        elif unit == 'year':
            result = self.num / 525600
        elif unit == 'decade':
            result = self.num / 5.256e6
        elif unit == 'century':
            result = self.num / 5.256e7
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result

# Hour
class Hour:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def hour_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 3.6e6
        elif unit == 'second':
            result = self.num * 3600
        elif unit == 'minute':
            result = self.num * 60
        elif unit == 'day':
            result = self.num / 24
        elif unit == 'week':
            result = self.num / 168
        elif unit == 'month':
            result = self.num / 730
        elif unit == 'year':
            result = self.num / 8760
        elif unit == 'decade':
            result = self.num / 87600
        elif unit == 'century':
            result = self.num / 876000
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result

# Day
class Day:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def day_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 86400000
        elif unit == 'second':
            result = self.num * 86400
        elif unit == 'minute':
            result = self.num * 1440
        elif unit == 'hour':
            result = self.num * 24
        elif unit == 'week':
            result = self.num / 7
        elif unit == 'month':
            result = self.num / 30.44  
        elif unit == 'year':
            result = self.num / 365.25  
        elif unit == 'decade':
            result = self.num / 3652.5  
        elif unit == 'century':
            result = self.num / 36525  
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result


# Week
class Week:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def week_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 604800000 
        elif unit == 'second':
            result = self.num * 604800
        elif unit == 'minute':
            result = self.num * 10080
        elif unit == 'hour':
            result = self.num * 168
        elif unit == 'day':
            result = self.num * 7
        elif unit == 'month':
            result = self.num / 4.348  
        elif unit == 'year':
            result = self.num / 52.1786 
        elif unit == 'decade':
            result = self.num / 521.786 
        elif unit == 'century':
            result = self.num / 5217.86  
        else:
            raise ValueError("Unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result


# Month
class Month:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def month_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 2.628e9  
        elif unit == 'second':
            result = self.num * 2.628e6
        elif unit == 'minute':
            result = self.num * 43800
        elif unit == 'hour':
            result = self.num * 730
        elif unit == 'day':
            result = self.num * 30.44
        elif unit == 'week':
            result = self.num * 4.348
        elif unit == 'year':
            result = self.num / 12
        elif unit == 'decade':
            result = self.num / 120
        elif unit == 'century':
            result = self.num / 1200
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result


# Year
class Year:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def year_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 3.154e10  
        elif unit == 'second':
            result = self.num * 3.154e7
        elif unit == 'minute':
            result = self.num * 525600
        elif unit == 'hour':
            result = self.num * 8760
        elif unit == 'day':
            result = self.num * 365.25
        elif unit == 'week':
            result = self.num * 52.1786
        elif unit == 'month':
            result = self.num * 12
        elif unit == 'decade':
            result = self.num / 10
        elif unit == 'century':
            result = self.num / 100
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'decade':
                return f"{result} dec"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result


# Decade
class Decade:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def decade_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 3.154e11  
        elif unit == 'second':
            result = self.num * 3.154e8
        elif unit == 'minute':
            result = self.num * 5.256e6
        elif unit == 'hour':
            result = self.num * 87600
        elif unit == 'day':
            result = self.num * 3652.5
        elif unit == 'week':
            result = self.num * 521.786
        elif unit == 'month':
            result = self.num * 120
        elif unit == 'year':
            result = self.num * 10
        elif unit == 'century':
            result = self.num / 10
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'century':
                return f"{result} cent"
        else:
            return result


# Century
class Century:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def century_to(self, unit: str) -> Union[float, str]:
        if unit == 'millisecond':
            result = self.num * 3.154e12 
        elif unit == 'second':
            result = self.num * 3.154e9
        elif unit == 'minute':
            result = self.num * 5.256e7
        elif unit == 'hour':
            result = self.num * 876000
        elif unit == 'day':
            result = self.num * 36525
        elif unit == 'week':
            result = self.num * 5217.86
        elif unit == 'month':
            result = self.num * 1200
        elif unit == 'year':
            result = self.num * 100
        elif unit == 'decade':
            result = self.num * 10
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'millisecond':
                return f"{result} ms"
            elif unit == 'second':
                return f"{result} sec"
            elif unit == 'minute':
                return f"{result} min"
            elif unit == 'hour':
                return f"{result} h"
            elif unit == 'day':
                return f"{result} d"
            elif unit == 'week':
                return f"{result} wk"
            elif unit == 'month':
                return f"{result} mo"
            elif unit == 'year':
                return f"{result} yr"
            elif unit == 'decade':
                return f"{result} dec"
        else:
            return result

