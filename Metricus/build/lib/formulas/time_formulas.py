# Second
class Second:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'minute':
            result = self.num / 60
        elif unit == 'hour':
            result = self.num / 3600
        elif unit == 'day':
            result = self.num / 86400
        elif unit == 'week':
            result = self.num / 604800
        elif unit == 'month':
            result = self.num / 2.628e6  # aprox. 30.44 days per month
        elif unit == 'year':
            result = self.num / 3.154e7  # 365.25 days per year
        elif unit == 'decade':
            result = self.num / 3.154e8  # 10 years
        elif unit == 'century':
            result = self.num / 3.154e9  # 100 years
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Minute
class Minute:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
            result = self.num * 60
        elif unit == 'hour':
            result = self.num / 60
        elif unit == 'day':
            result = self.num / 1440
        elif unit == 'week':
            result = self.num / 10080
        elif unit == 'month':
            result = self.num / 43800  # aprox. minutes per month
        elif unit == 'year':
            result = self.num / 525600  # minutes per year
        elif unit == 'decade':
            result = self.num / 5.256e6  # 10 years
        elif unit == 'century':
            result = self.num / 5.256e7  # 100 years
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Hour
class Hour:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
            result = self.num * 3600
        elif unit == 'minute':
            result = self.num * 60
        elif unit == 'day':
            result = self.num / 24
        elif unit == 'week':
            result = self.num / 168
        elif unit == 'month':
            result = self.num / 730  # aprox. hours per month
        elif unit == 'year':
            result = self.num / 8760  # hours per year
        elif unit == 'decade':
            result = self.num / 87600  # 10 years
        elif unit == 'century':
            result = self.num / 876000  # 100 years
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"
# Day
class Day:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
            result = self.num * 86400
        elif unit == 'minute':
            result = self.num * 1440
        elif unit == 'hour':
            result = self.num * 24
        elif unit == 'week':
            result = self.num / 7
        elif unit == 'month':
            result = self.num / 30.44  # aprox. days per month
        elif unit == 'year':
            result = self.num / 365.25  # days per year
        elif unit == 'decade':
            result = self.num / 3652.5  # 10 years
        elif unit == 'century':
            result = self.num / 36525  # 100 years
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Week
class Week:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
            result = self.num * 604800
        elif unit == 'minute':
            result = self.num * 10080
        elif unit == 'hour':
            result = self.num * 168
        elif unit == 'day':
            result = self.num * 7
        elif unit == 'month':
            result = self.num / 4.348  # weeks per month
        elif unit == 'year':
            result = self.num / 52.1786  # weeks per year
        elif unit == 'decade':
            result = self.num / 521.786  # 10 years
        elif unit == 'century':
            result = self.num / 5217.86  # 100 years
        else:
            raise ValueError("Unknown unit")
        return f"{result} {unit}"


# Month
class Month:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
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
        return f"{result} {unit}"


# Year
class Year:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
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
        return f"{result} {unit}"


# Decade
class Decade:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
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
        return f"{result} {unit}"


# Century
class Century:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'second':
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
        return f"{result} {unit}"













