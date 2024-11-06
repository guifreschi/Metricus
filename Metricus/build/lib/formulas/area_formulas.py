# SquareCentimeter
class SquareCentimeter:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num / 10000
        elif unit == 'square_foot':
            result = self.num / 929.0304
        elif unit == 'square_yard':
            result = self.num / 8361.2736
        elif unit == 'hectare':
            result = self.num / 1e8
        elif unit == 'acre':
            result = self.num / 4.04686e7
        elif unit == 'square_kilometer':
            result = self.num / 1e10
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# SquareFoot
class SquareFoot:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num / 10.7639
        elif unit == 'square_centimeter':
            result = self.num * 929.0304
        elif unit == 'square_yard':
            result = self.num / 9
        elif unit == 'hectare':
            result = self.num / 107639
        elif unit == 'acre':
            result = self.num / 43560
        elif unit == 'square_kilometer':
            result = self.num / 1.076e7
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# SquareYard
class SquareYard:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num / 1.19599
        elif unit == 'square_centimeter':
            result = self.num * 8361.2736
        elif unit == 'square_foot':
            result = self.num * 9
        elif unit == 'hectare':
            result = self.num / 11959.9
        elif unit == 'acre':
            result = self.num / 4840
        elif unit == 'square_kilometer':
            result = self.num / 1.196e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# SquareMeter
class SquareMeter:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_centimeter':
            result = self.num * 10000
        elif unit == 'square_foot':
            result = self.num * 10.7639
        elif unit == 'square_yard':
            result = self.num * 1.19599
        elif unit == 'hectare':
            result = self.num / 10000
        elif unit == 'acre':
            result = self.num / 4046.86
        elif unit == 'square_kilometer':
            result = self.num / 1e6
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Hectare
class Hectare:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num * 10000
        elif unit == 'square_centimeter':
            result = self.num * 1e8
        elif unit == 'square_foot':
            result = self.num * 107639
        elif unit == 'square_yard':
            result = self.num * 11959.9
        elif unit == 'acre':
            result = self.num * 2.47105
        elif unit == 'square_kilometer':
            result = self.num / 100
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# Acre
class Acre:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num * 4046.86
        elif unit == 'square_centimeter':
            result = self.num * 4.04686e7
        elif unit == 'square_foot':
            result = self.num * 43560
        elif unit == 'square_yard':
            result = self.num * 4840
        elif unit == 'hectare':
            result = self.num / 2.47105
        elif unit == 'square_kilometer':
            result = self.num / 247.105
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"


# SquareKilometer
class SquareKilometer:
    def __init__(self, num: float) -> None:
        self.num = num

    def to(self, unit: str) -> str:
        if unit == 'square_meter':
            result = self.num * 1e6
        elif unit == 'square_centimeter':
            result = self.num * 1e10
        elif unit == 'square_foot':
            result = self.num * 1.076e7
        elif unit == 'square_yard':
            result = self.num * 1.196e6
        elif unit == 'hectare':
            result = self.num * 100
        elif unit == 'acre':
            result = self.num * 247.105
        else:
            raise ValueError("The measurement has an unknown unit")
        return f"{result} {unit}"
