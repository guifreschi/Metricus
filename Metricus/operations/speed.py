from formulas import speed_formulas as sf
from typing import Union

unit_list = ['meters_per_second', 'kilometers_per_hour', 'miles_per_hour', 'knots']

def speed_converter(speed: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit == 'meters_per_second':
            return sf.MetersPerSecond(speed, with_unit=with_unit).meters_per_second_to(to_unit)
        elif from_unit == 'kilometers_per_hour':
            return sf.KilometersPerHour(speed, with_unit=with_unit).kilometers_per_hour_to(to_unit)
        elif from_unit == 'miles_per_hour':
            return sf.MilesPerHour(speed, with_unit=with_unit).miles_per_hour_to(to_unit)
        elif from_unit == 'knots':
            return sf.Knots(speed, with_unit=with_unit).knots_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")
