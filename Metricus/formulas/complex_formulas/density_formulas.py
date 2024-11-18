from typing import Union
from formulas import mass_formulas
from formulas import volume_formulas

def density_calculator(mass: float, volume: float, density_unit: str, with_unit: bool = False) -> Union[float, str]:
    result = mass / volume

    if density_unit == 'kg/m³':
        return f"{result} kg/m³" if with_unit else result

    units = {
        'g/cm³': result / 1000,
        'lb/ft³': result * 0.062428,
        'oz/in³': result * 0.0005780367,
    }

    if density_unit in units:
        return f"{units[density_unit]} {density_unit}" if with_unit else units[density_unit]

    raise ValueError(f"Unknown unit: {density_unit}")
