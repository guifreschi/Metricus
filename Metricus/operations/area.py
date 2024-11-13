from formulas import area_formulas as af
from typing import Union

unit_list = ['square_centimeter','square_foot','square_meter','square_yard','acre','hectare','square_kilometer']

def area_converter(area: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
  if from_unit not in unit_list or to_unit not in unit_list:  
    raise ValueError("The measurement has an unknown unit")
  else:
    if from_unit == 'square_centimeter':
      return af.SquareCentimeter(area, with_unit=with_unit).square_centimeter_to(to_unit)
    elif from_unit == 'square_foot':
      return af.SquareFoot(area, with_unit=with_unit).square_foot_to(to_unit)
    elif from_unit == 'square_meter':
      return af.SquareMeter(area, with_unit=with_unit).square_meter_to(to_unit)
    elif from_unit == 'square_yard':
      return af.SquareYard(area, with_unit=with_unit).square_yard_to(to_unit)
    elif from_unit == 'acre':
      return af.Acre(area, with_unit=with_unit).acre_to(to_unit)
    elif from_unit == 'hectare':
      return af.Hectare(area, with_unit=with_unit).hectare_to(to_unit)
    elif from_unit == 'square_kilometer':
      return af.SquareKilometer(area, with_unit=with_unit).square_kilometer_to(to_unit)
    else:
      raise ValueError("The measurement has an unknown unit")
