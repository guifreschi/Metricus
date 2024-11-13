from formulas import mass_formulas as mf
from typing import Union

unit_list = [
    'milligram', 'carat', 'gram', 'ounce', 
    'pound', 'kilogram', 'stone', 'slug', 'tonne'
]

def mass_converter(value: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit == 'milligram':
            return mf.Milligram(value, with_unit=with_unit).milligram_to(to_unit)
        elif from_unit == 'carat':
            return mf.Carat(value, with_unit=with_unit).carat_to(to_unit)
        elif from_unit == 'gram':
            return mf.Gram(value, with_unit=with_unit).gram_to(to_unit)
        elif from_unit == 'ounce':
            return mf.Ounce(value, with_unit=with_unit).ounce_to(to_unit)
        elif from_unit == 'pound':
            return mf.Pound(value, with_unit=with_unit).pound_to(to_unit)
        elif from_unit == 'kilogram':
            return mf.Kilogram(value, with_unit=with_unit).kilogram_to(to_unit)
        elif from_unit == 'stone':
            return mf.Stone(value, with_unit=with_unit).stone_to(to_unit)
        elif from_unit == 'slug':
            return mf.Slug(value, with_unit=with_unit).slug_to(to_unit)
        elif from_unit == 'tonne':
            return mf.Tonne(value, with_unit=with_unit).tonne_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")
