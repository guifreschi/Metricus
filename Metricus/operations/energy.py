from typing import Union

# Supported energy units
unit_list = ['electronvolt', 'calorie', 'joule', 'british_thermal_unit', 'kilocalorie', 'kilowatt_hour']

class Electronvolt:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def electronvolt_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'calorie': 3.829e-20,
            'joule': 1.60218e-19,
            'british_thermal_unit': 1.5186e-22,
            'kilocalorie': 3.829e-23,
            'kilowatt_hour': 4.4505e-26
        }
        return self._convert(conversion_factors, to_unit)

class Calorie:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def calorie_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'electronvolt': 2.611e19,
            'joule': 4.184,
            'british_thermal_unit': 0.00396567,
            'kilocalorie': 0.001,
            'kilowatt_hour': 1.16279e-6
        }
        return self._convert(conversion_factors, to_unit)

class Joule:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def joule_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'electronvolt': 6.242e18,
            'calorie': 0.239006,
            'british_thermal_unit': 0.000947817,
            'kilocalorie': 0.000239006,
            'kilowatt_hour': 2.77778e-7
        }
        return self._convert(conversion_factors, to_unit)

class BritishThermalUnit:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def british_thermal_unit_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'electronvolt': 6.5851e21,
            'calorie': 252.164,
            'joule': 1055.06,
            'kilocalorie': 0.252164,
            'kilowatt_hour': 0.000293071
        }
        return self._convert(conversion_factors, to_unit)

class Kilocalorie:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def kilocalorie_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'electronvolt': 2.611e22,
            'calorie': 1000,
            'joule': 4184,
            'british_thermal_unit': 3.96567,
            'kilowatt_hour': 0.00116279
        }
        return self._convert(conversion_factors, to_unit)

class KilowattHour:
    def __init__(self, value: float, with_unit: bool = False):
        self.value = value
        self.with_unit = with_unit

    def kilowatt_hour_to(self, to_unit: str) -> Union[float, str]:
        conversion_factors = {
            'electronvolt': 2.247e25,
            'calorie': 860420,
            'joule': 3.6e6,
            'british_thermal_unit': 3412.14,
            'kilocalorie': 860.42
        }
        return self._convert(conversion_factors, to_unit)

def energy_converter(value: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    """
    Converts energy from one unit to another.

    Parameters:
        value (float): The energy value to be converted.
        from_unit (str): The original unit of energy (electronvolt, calorie, joule, british_thermal_unit, kilocalorie, kilowatt_hour).
        to_unit (str): The target unit of energy (electronvolt, calorie, joule, british_thermal_unit, kilocalorie, kilowatt_hour).
        with_unit (bool, optional): If true, returns the energy with the unit. Default is False.

    Returns:
        Union[float, str]: The converted energy, with or without unit.

    Raises:
        ValueError: If the original or target unit is unknown.
    """
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("Unknown unit of measurement")
    else:
        if from_unit == 'electronvolt':
            return Electronvolt(value, with_unit=with_unit).electronvolt_to(to_unit)
        elif from_unit == 'calorie':
            return Calorie(value, with_unit=with_unit).calorie_to(to_unit)
        elif from_unit == 'joule':
            return Joule(value, with_unit=with_unit).joule_to(to_unit)
        elif from_unit == 'british_thermal_unit':
            return BritishThermalUnit(value, with_unit=with_unit).british_thermal_unit_to(to_unit)
        elif from_unit == 'kilocalorie':
            return Kilocalorie(value, with_unit=with_unit).kilocalorie_to(to_unit)
        elif from_unit == 'kilowatt_hour':
            return KilowattHour(value, with_unit=with_unit).kilowatt_hour_to(to_unit)
        else:
            raise ValueError("Unknown unit of measurement")

