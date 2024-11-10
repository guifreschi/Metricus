from typing import Union

# Pascal
class Pascal:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
            raise ValueError("The measurement has an unknown unit")
    
        if self.with_unit:
            if unit == 'atmosphere':
                return f"{result} atm"
            else:
                return f"{result} {unit}"
        else:
            return result


# Millimeter of Mercury
class MillimeterOfMercury:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
            raise ValueError("The measurement has an unknown unit")
    
        if self.with_unit:
            if unit == 'atmosphere':
                return f"{result} atm"
            else:
                return f"{result} {unit}"
        else:
            return result


# Pound-force per Square Inch
class PoundForcePerSquareInch:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
            raise ValueError("The measurement has an unknown unit")
    
        if self.with_unit:
            return f"{result} {unit}"
        else:
            return result


# Bar
class Bar:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
            raise ValueError("The measurement has an unknown unit")
    
        if self.with_unit:
            if unit == 'atmosphere':
                return f"{result} atm"
            else:
                return f"{result} {unit}"
        else:
            return result


# Atmosphere
class Atmosphere:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
            raise ValueError("The measurement has an unknown unit")
    
        if self.with_unit:
            if unit == 'pascal':
                return f"{result} Pa"
            else:
                return f"{result} {unit}"
        else:
            return result
