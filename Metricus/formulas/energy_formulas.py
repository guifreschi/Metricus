from typing import Union

# Classe base para Energia
class EnergyUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        units_map = {
            "electronvolt": "eV",
            "calorie": "cal",
            "joule": "J",
            "btu": "BTU",
            "kilocalorie": "kcal",
            "kilowatt_hour": "kWh",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result

# Electronvolt 
class Electronvolt(EnergyUnit):
    def electronvolt_to(self, unit: str) -> Union[float, str]:
        if unit == 'calorie':
            result = self.num * 1.60218e-19 / 4.184
        elif unit == 'joule':
            result = self.num * 1.60218e-19
        elif unit == 'btu':
            result = self.num * 1.60218e-19 / 1055.06
        elif unit == 'kilocalorie':
            result = self.num * 1.60218e-19 / (4.184 * 1000)
        elif unit == 'kilowatt_hour':
            result = self.num * 1.60218e-19 / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Calorie 
class Calorie(EnergyUnit):
    def calorie_to(self, unit: str) -> Union[float, str]:
        if unit == 'electronvolt':
            result = self.num * 4.184 / 1.60218e-19
        elif unit == 'joule':
            result = self.num * 4.184
        elif unit == 'btu':
            result = self.num * 4.184 / 1055.06
        elif unit == 'kilocalorie':
            result = self.num / 1000
        elif unit == 'kilowatt_hour':
            result = self.num * 4.184 / 3.6e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Joule 
class Joule(EnergyUnit):
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
        return self.format_result(result, unit)  # Add this line to return the result

# British Thermal Unit 
class BritishThermalUnit(EnergyUnit):
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
        return self.format_result(result, unit)

# Kilocalorie 
class Kilocalorie(EnergyUnit):
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
        return self.format_result(result, unit)

# Kilowatt-hour 
class KilowattHour(EnergyUnit):
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
        return self.format_result(result, unit)
