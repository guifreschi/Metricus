from formulas import length_formulas as lf
from typing import Union

unit_list = [
    'millimeter', 'centimeter', 'inch', 'foot', 
    'yard', 'meter', 'kilometer', 'mile', 'nautical_mile'
]

def length_converter(length: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit == 'millimeter':
            return lf.Millimeter(length, with_unit=with_unit).millimeter_to(to_unit)
        elif from_unit == 'centimeter':
            return lf.Centimeter(length, with_unit=with_unit).centimeter_to(to_unit)
        elif from_unit == 'inch':
            return lf.Inch(length, with_unit=with_unit).inch_to(to_unit)
        elif from_unit == 'foot':
            return lf.Foot(length, with_unit=with_unit).foot_to(to_unit)
        elif from_unit == 'yard':
            return lf.Yard(length, with_unit=with_unit).yard_to(to_unit)
        elif from_unit == 'meter':
            return lf.Meter(length, with_unit=with_unit).meter_to(to_unit)
        elif from_unit == 'kilometer':
            return lf.Kilometer(length, with_unit=with_unit).kilometer_to(to_unit)
        elif from_unit == 'mile':
            return lf.Mile(length, with_unit=with_unit).mile_to(to_unit)
        elif from_unit == 'nautical_mile':
            return lf.NauticalMile(length, with_unit=with_unit).nautical_mile_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")
