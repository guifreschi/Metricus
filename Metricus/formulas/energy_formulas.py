from typing import Union

# Electronvolt
class Electronvolt:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def electronvolt_to(self, unit: str) -> Union[float, str]:
        if unit == 'calorie':
            result = (self.num * 1.60218e-19) / 4.184
        elif unit == 'joule':
            result = self.num * 1.60218e-19
        elif unit == 'btu':
            result = (self.num * 1.60218e-19) / 1055.06
        elif unit == 'kilocalorie':
            result = (self.num * 1.60218e-19) / (4.184 * 1000)
        elif unit == 'kilowatt_hour':
            result = (self.num * 1.60218e-19) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "calorie":
                return f"{result} cal"
            elif unit == "joule":
                return f"{result} J"
            elif unit == "btu":
                return f"{result} BTU"
            elif unit == "kilocalorie":
                return f"{result} kcal"
            elif unit == "kilowatt_hour":
                return f"{result} kWh"
        else:
            return result


# Calorie
class Calorie:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def calorie_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = (self.num * 4.184) / 1.60218e-19
        elif unit == 'joule':
            result = self.num * 4.184
        elif unit == 'btu':
            result = (self.num * 4.184) / 1055.06
        elif unit == 'kilocalorie':
            result = self.num / 1000
        elif unit == 'kilowatt_hour':
            result = (self.num * 4.184) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'electronvolt':
                return f"{result} eV"
            elif unit == 'joule':
                return f"{result} J"
            elif unit == 'btu':
                return f"{result} BTU"
            elif unit == 'kilocalorie':
                return f"{result} kcal"
            elif unit == 'kilowatt_hour':
                return f"{result} kWh"
        else:
            return result


# Joule
class Joule:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def joule_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = self.num / 1.60218e-19
        elif unit == 'calorie':
            result = self.num / 4.184
        elif unit == 'btu':
            result = self.num / 1055.06
        elif unit == 'kilocalorie':
            result = self.num / (4.184 * 1000)
        elif unit == 'kilowatt_hour':
            result = self.num / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'electronvolt':
                return f"{result} eV"
            elif unit == 'calorie':
                return f"{result} cal"
            elif unit == 'btu':
                return f"{result} BTU"
            elif unit == 'kilocalorie':
                return f"{result} kcal"
            elif unit == 'kilowatt_hour':
                return f"{result} kWh"
        else:
            return result


# British Thermal Unit
class BritishThermalUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def btu_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = (self.num * 1055.06) / 1.60218e-19
        elif unit == 'calorie':
            result = (self.num * 1055.06) / 4.184
        elif unit == 'joule':
            result = self.num * 1055.06
        elif unit == 'kilocalorie':
            result = (self.num * 1055.06) / (4.184 * 1000)
        elif unit == 'kilowatt_hour':
            result = (self.num * 1055.06) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'electronvolt':
                return f"{result} eV"
            elif unit == 'calorie':
                return f"{result} cal"
            elif unit == 'joule':
                return f"{result} J"
            elif unit == 'kilocalorie':
                return f"{result} kcal"
            elif unit == 'kilowatt_hour':
                return f"{result} kWh"
        else:
            return result


# Kilocalorie
class Kilocalorie:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def kilocalorie_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = (self.num * 4184) / 1.60218e-19
        elif unit == 'calorie':
            result = self.num * 1000
        elif unit == 'joule':
            result = self.num * 4184
        elif unit == 'btu':
            result = (self.num * 4184) / 1055.06
        elif unit == 'kilowatt_hour':
            result = (self.num * 4184) / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'electronvolt':
                return f"{result} eV"
            elif unit == 'calorie':
                return f"{result} cal"
            elif unit == 'joule':
                return f"{result} J"
            elif unit == 'btu':
                return f"{result} BTU"
            elif unit == 'kilowatt_hour':
                return f"{result} kWh"
        else:
            return result

# Kilowatt-hour
class KilowattHour:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def kilowatt_hour_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = (self.num * 3.6e6) / 1.60218e-19
        elif unit == 'calorie':
            result = (self.num * 3.6e6) / 4.184
        elif unit == 'joule':
            result = self.num * 3.6e6
        elif unit == 'btu':
            result = (self.num * 3.6e6) / 1055.06
        elif unit == 'kilocalorie':
            result = (self.num * 3.6e6) / (4.184 * 1000)
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'electronvolt':
                return f"{result} eV"
            elif unit == 'calorie':
                return f"{result} cal"
            elif unit == 'joule':
                return f"{result} J"
            elif unit == 'btu':
                return f"{result} BTU"
            elif unit == 'kilocalorie':
                return f"{result} kcal"
        else:
            return result

