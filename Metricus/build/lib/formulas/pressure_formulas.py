# Pascal
class Pascal:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'bar':
            result = self.num / 100000
        elif unit == 'atmosphere':
            result = self.num / 101325
        elif unit == 'mmHg':
            result = self.num / 133.322
        elif unit == 'psi':
            result = self.num / 6894.76
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Bar
class Bar:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'pascal':
            result = self.num * 100000
        elif unit == 'atmosphere':
            result = self.num / 1.01325
        elif unit == 'mmHg':
            result = (self.num * 100000) / 133.322
        elif unit == 'psi':
            result = (self.num * 100000) / 6894.76
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Atmosphere
class Atmosphere:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'pascal':
            result = self.num * 101325
        elif unit == 'bar':
            result = self.num * 1.01325
        elif unit == 'mmHg':
            result = self.num * 760
        elif unit == 'psi':
            result = self.num * 14.6959
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Millimeter of Mercury
class MillimeterOfMercury:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'pascal':
            result = self.num * 133.322
        elif unit == 'bar':
            result = (self.num * 133.322) / 100000
        elif unit == 'atmosphere':
            result = self.num / 760
        elif unit == 'psi':
            result = (self.num * 133.322) / 6894.76
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Pound-force per Square Inch
class PoundForcePerSquareInch:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'pascal':
            result = self.num * 6894.76
        elif unit == 'bar':
            result = (self.num * 6894.76) / 100000
        elif unit == 'atmosphere':
            result = self.num / 14.6959
        elif unit == 'mmHg':
            result = (self.num * 6894.76) / 133.322
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"
