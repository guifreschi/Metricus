from formulas import energy_formulas as ef
from typing import Union

unit_list = ['electronvolt', 'calorie', 'joule', 'british_thermal_unit', 'kilocalorie', 'kilowatt_hour']

def energy_converter(energy: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("Unknown unit of measurement")
    else:
        if from_unit == 'electronvolt':
            return ef.Electronvolt(energy, with_unit=with_unit).electronvolt_to(to_unit)
        elif from_unit == 'calorie':
            return ef.Calorie(energy, with_unit=with_unit).calorie_to(to_unit)
        elif from_unit == 'joule':
            return ef.Joule(energy, with_unit=with_unit).joule_to(to_unit)
        elif from_unit == 'british_thermal_unit':
            return ef.BritishThermalUnit(energy, with_unit=with_unit).british_thermal_unit_to(to_unit)
        elif from_unit == 'kilocalorie':
            return ef.Kilocalorie(energy, with_unit=with_unit).kilocalorie_to(to_unit)
        elif from_unit == 'kilowatt_hour':
            return ef.KilowattHour(energy, with_unit=with_unit).kilowatt_hour_to(to_unit)
        else:
            raise ValueError("Unknown unit of measurement")
