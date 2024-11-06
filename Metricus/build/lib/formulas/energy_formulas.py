# Joule
class Joule:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'calorie':
            result = self.num / 4.184
        elif unit == 'electronvolt':
            result = self.num / 1.60218e-19
        elif unit == 'btu':
            result = self.num / 1055.06
        elif unit == 'kilowatt_hour':
            result = self.num / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Calorie
class Calorie:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'joule':
            result = self.num * 4.184
        elif unit == 'electronvolt':
            result = (self.num * 4.184) / 1.60218e-19
        elif unit == 'btu':
            result = (self.num * 4.184) / 1055.06
        elif unit == 'kilowatt_hour':
            result = (self.num * 4.184) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Electronvolt
class Electronvolt:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'joule':
            result = self.num * 1.60218e-19
        elif unit == 'calorie':
            result = (self.num * 1.60218e-19) / 4.184
        elif unit == 'btu':
            result = (self.num * 1.60218e-19) / 1055.06
        elif unit == 'kilowatt_hour':
            result = (self.num * 1.60218e-19) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# British Thermal Unit
class BritishThermalUnit:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'joule':
            result = self.num * 1055.06
        elif unit == 'calorie':
            result = (self.num * 1055.06) / 4.184
        elif unit == 'electronvolt':
            result = (self.num * 1055.06) / 1.60218e-19
        elif unit == 'kilowatt_hour':
            result = (self.num * 1055.06) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"

# Kilowatt-hour
class KilowattHour:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'joule':
            result = self.num * 3.6e6
        elif unit == 'calorie':
            result = (self.num * 3.6e6) / 4.184
        elif unit == 'electronvolt':
            result = (self.num * 3.6e6) / 1.60218e-19
        elif unit == 'btu':
            result = (self.num * 3.6e6) / 1055.06
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"
