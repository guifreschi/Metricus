from formulas import pressure_formulas as pf
from typing import Union

unit_list = ['pascal', 'millimeter_of_mercury', 'pound_force_per_square_inch', 'bar', 'atmosphere']

def pressure_converter(pressure: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit == 'pascal':
            return pf.Pascal(pressure, with_unit=with_unit).pascal_to(to_unit)
        elif from_unit == 'millimeter_of_mercury':
            return pf.MillimeterOfMercury(pressure, with_unit=with_unit).millimeter_of_mercury_to(to_unit)
        elif from_unit == 'pound_force_per_square_inch':
            return pf.PoundForcePerSquareInch(pressure, with_unit=with_unit).pound_force_per_square_inch_to(to_unit)
        elif from_unit == 'bar':
            return pf.Bar(pressure, with_unit=with_unit).bar_to(to_unit)
        elif from_unit == 'atmosphere':
            return pf.Atmosphere(pressure, with_unit=with_unit).atmosphere_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")
