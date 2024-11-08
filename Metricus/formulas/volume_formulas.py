from typing import Union

# Classe base para Volume
class Volume:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        return f"{result} {unit}" if self.with_unit else result

# Milliliter (mL)
class Milliliter(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'cm³':
            result = self.num
        elif unit == 'fl oz':
            result = self.num / 29.5735
        elif unit == 'cup':
            result = self.num / 240
        elif unit == 'pt':
            result = self.num / 473.176
        elif unit == 'qt':
            result = self.num / 946.353
        elif unit == 'L':
            result = self.num / 1000
        elif unit == 'gal':
            result = self.num / 3785.41
        elif unit == 'bbl':
            result = self.num / 119240
        elif unit == 'm³':
            result = self.num / 1e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Cubic Centimeter (cm³)
class CubicCentimeter(Volume):
    def to(self, unit: str) -> Union[float, str]:
        # cm³ é equivalente a mL
        return Milliliter(self.num, self.with_unit).to(unit)

# Fluid Ounce (fl oz)
class FluidOunce(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 29.5735
        elif unit == 'cm³':
            result = self.num * 29.5735
        elif unit == 'cup':
            result = self.num / 8
        elif unit == 'pt':
            result = self.num / 16
        elif unit == 'qt':
            result = self.num / 32
        elif unit == 'L':
            result = self.num / 33.814
        elif unit == 'gal':
            result = self.num / 128
        elif unit == 'bbl':
            result = self.num / 4032
        elif unit == 'm³':
            result = self.num / 33814
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Cup (cup)
class Cup(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 240
        elif unit == 'cm³':
            result = self.num * 240
        elif unit == 'fl oz':
            result = self.num * 8
        elif unit == 'pt':
            result = self.num / 2
        elif unit == 'qt':
            result = self.num / 4
        elif unit == 'L':
            result = self.num / 4.22675
        elif unit == 'gal':
            result = self.num / 16
        elif unit == 'bbl':
            result = self.num / 5040
        elif unit == 'm³':
            result = self.num / 4226.75
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Pint (pt)
class Pint(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 473.176
        elif unit == 'cm³':
            result = self.num * 473.176
        elif unit == 'fl oz':
            result = self.num * 16
        elif unit == 'cup':
            result = self.num * 2
        elif unit == 'qt':
            result = self.num / 2
        elif unit == 'L':
            result = self.num / 2.11338
        elif unit == 'gal':
            result = self.num / 8
        elif unit == 'bbl':
            result = self.num / 2016
        elif unit == 'm³':
            result = self.num / 2113.38
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Quart (qt)
class Quart(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 946.353
        elif unit == 'cm³':
            result = self.num * 946.353
        elif unit == 'fl oz':
            result = self.num * 32
        elif unit == 'cup':
            result = self.num * 4
        elif unit == 'pt':
            result = self.num * 2
        elif unit == 'L':
            result = self.num / 1.05669
        elif unit == 'gal':
            result = self.num / 4
        elif unit == 'bbl':
            result = self.num / 1008
        elif unit == 'm³':
            result = self.num / 1056.69
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Liter (L)
class Liter(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 1000
        elif unit == 'cm³':
            result = self.num * 1000
        elif unit == 'fl oz':
            result = self.num * 33.814
        elif unit == 'cup':
            result = self.num * 4.22675
        elif unit == 'pt':
            result = self.num * 2.11338
        elif unit == 'qt':
            result = self.num * 1.05669
        elif unit == 'gal':
            result = self.num / 3.78541
        elif unit == 'bbl':
            result = self.num / 119.24
        elif unit == 'm³':
            result = self.num / 1000
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Gallon (gal)
class Gallon(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 3785.41
        elif unit == 'cm³':
            result = self.num * 3785.41
        elif unit == 'fl oz':
            result = self.num * 128
        elif unit == 'cup':
            result = self.num * 16
        elif unit == 'pt':
            result = self.num * 8
        elif unit == 'qt':
            result = self.num * 4
        elif unit == 'L':
            result = self.num * 3.78541
        elif unit == 'bbl':
            result = self.num / 31.5
        elif unit == 'm³':
            result = self.num / 264.172
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Barrel (bbl)
class Barrel(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 119240
        elif unit == 'cm³':
            result = self.num * 119240
        elif unit == 'fl oz':
            result = self.num * 4032
        elif unit == 'cup':
            result = self.num * 5040
        elif unit == 'pt':
            result = self.num * 2016
        elif unit == 'qt':
            result = self.num * 1008
        elif unit == 'L':
            result = self.num * 119.24
        elif unit == 'gal':
            result = self.num * 31.5
        elif unit == 'm³':
            result = self.num / 8.386
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Cubic Meter (m³)
class CubicMeter(Volume):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'mL':
            result = self.num * 1e6
        elif unit == 'cm³':
            result = self.num * 1e6
        elif unit == 'fl oz':
            result = self.num * 33814
        elif unit == 'cup':
            result = self.num * 4226.75
        elif unit == 'pt':
            result = self.num * 2113.38
        elif unit == 'qt':
            result = self.num * 1056.69