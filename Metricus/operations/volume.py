from formulas import volume_formulas as vf
from typing import Union

unit_list = [
    "mL",
    "cm3",
    "cm³",
    "fl_oz",
    "cup",
    "pt",
    "qt",
    "L",
    "gal",
    "bbl",
    "m3",
    "m³"
]

def volume_converter(volume: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
  if from_unit not in unit_list or to_unit not in unit_list:
    raise ValueError("The measurement has an unknown unit")

  if from_unit == 'mL':
    return vf.Milliliter(volume, with_unit=with_unit).mL_to(to_unit)
  elif from_unit == 'cm3' or from_unit == 'cm³':
    return vf.Milliliter(volume, with_unit=with_unit).mL_to(to_unit)
  elif from_unit == 'fl_oz':
    return vf.FluidOunce(volume, with_unit=with_unit).fl_oz_to(to_unit)
  elif from_unit == 'cup':
    return vf.Cup(volume, with_unit=with_unit).cup_to(to_unit)
  elif from_unit == 'pt':
    return vf.Pint(volume, with_unit=with_unit).pt_to(to_unit)
  elif from_unit == 'qt':
    return vf.Quart(volume, with_unit=with_unit).qt_to(to_unit)
  elif from_unit == 'L':
    return vf.Liter(volume, with_unit=with_unit).liter_to(to_unit)
  elif from_unit == 'gal':
    return vf.Gallon(volume, with_unit=with_unit).gal_to(to_unit)
  elif from_unit == 'bbl':
    return vf.Barrel(volume, with_unit=with_unit).bbl_to(to_unit)
  elif from_unit == 'm3' or from_unit == 'm³':
    return vf.CubicMeter(volume, with_unit=with_unit).m3_to(to_unit)
