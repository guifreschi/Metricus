from typing import Union


# Classe base para unidades de pressão
class PressureUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        units_map = {
            "pascal": "Pa",
            "mmHg": "mmHg",
            "psi": "psi",
            "bar": "bar",
            "atmosphere": "atm",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result


# Pascal
class Pascal(PressureUnit):
    def pascal_to(self, unit: str) -> Union[float, str]:
        if unit == 'mmHg':
            result = self.num / 133.322
        elif unit == 'psi':
            result = self.num / 6894.76
        elif unit == 'bar':
            result = self.num / 100000
        elif unit == 'atmosphere':
            result = self.num / 101325
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Millimeter of Mercury
class MillimeterOfMercury(PressureUnit):
    def mmHg_to(self, unit: str) -> Union[float, str]:
        if unit == 'pascal':
            result = self.num * 133.322
        elif unit == 'psi':
            result = (self.num * 133.322) / 6894.76
        elif unit == 'bar':
            result = (self.num * 133.322) / 100000
        elif unit == 'atmosphere':
            result = self.num / 760
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Pound-force per Square Inch
class PoundForcePerSquareInch(PressureUnit):
    def psi_to(self, unit: str) -> Union[float, str]:
        if unit == 'pascal':
            result = self.num * 6894.76
        elif unit == 'mmHg':
            result = (self.num * 6894.76) / 133.322
        elif unit == 'bar':
            result = (self.num * 6894.76) / 100000
        elif unit == 'atmosphere':
            result = self.num / 14.6959
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Bar
class Bar(PressureUnit):
    def bar_to(self, unit: str) -> Union[float, str]:
        if unit == 'pascal':
            result = self.num * 100000
        elif unit == 'mmHg':
            result = (self.num * 100000) / 133.322
        elif unit == 'psi':
            result = (self.num * 100000) / 6894.76
        elif unit == 'atmosphere':
            result = self.num / 1.01325
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Atmosphere
class Atmosphere(PressureUnit):
    def atmosphere_to(self, unit: str) -> Union[float, str]:
        if unit == 'pascal':
            result = self.num * 101325
        elif unit == 'mmHg':
            result = self.num * 760
        elif unit == 'psi':
            result = self.num * 14.6959
        elif unit == 'bar':
            result = self.num * 1.01325
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)
