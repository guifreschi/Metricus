from typing import Union

# SquareCentimeter
class SquareCentimeter:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def square_centimeter_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_foot':
            result = self.num / 929.0304
        elif unit == 'square_meter':
            result = self.num / 10000
        elif unit == 'square_yard':
            result = self.num / 8361.2736
        elif unit == 'acre':
            result = self.num / 4.04686e7
        elif unit == 'hectare':
            result = self.num / 1e8
        elif unit == 'square_kilometer':
            result = self.num / 1e10
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "hectare":
                return f"{result} ha"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# SquareFoot
class SquareFoot:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def square_foot_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 929.0304
        elif unit == 'square_meter':
            result = self.num / 10.7639
        elif unit == 'square_yard':
            result = self.num / 9
        elif unit == 'acre':
            result = self.num / 43560
        elif unit == 'hectare':
            result = self.num / 107639
        elif unit == 'square_kilometer':
            result = self.num / 1.076e7
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "hectare":
                return f"{result} ha"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# SquareYard
class SquareYard:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def square_yard_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 8361.2736
        elif unit == 'square_foot':
            result = self.num * 9
        elif unit == 'square_meter':
            result = self.num / 1.19599
        elif unit == 'acre':
            result = self.num / 4840
        elif unit == 'hectare':
            result = self.num / 11959.9
        elif unit == 'square_kilometer':
            result = self.num / 1.196e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "hectare":
                return f"{result} ha"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# SquareMeter
class SquareMeter:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def square_meter_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 10000
        elif unit == 'square_foot':
            result = self.num * 10.7639
        elif unit == 'square_yard':
            result = self.num * 1.19599
        elif unit == 'acre':
            result = self.num / 4046.86
        elif unit == 'hectare':
            result = self.num / 10000
        elif unit == 'square_kilometer':
            result = self.num / 1e6
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "hectare":
                return f"{result} ha"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# Acre
class Acre:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def acre_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 4.04686e7
        elif unit == 'square_foot':
            result = self.num * 43560
        elif unit == 'square_yard':
            result = self.num * 4840
        elif unit == 'square_meter':
            result = self.num * 4046.86
        elif unit == 'hectare':
            result = self.num / 2.47105
        elif unit == 'square_kilometer':
            result = self.num / 247.105
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "hectare":
                return f"{result} ha"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# Hectare
class Hectare:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def hectare_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 1e8
        elif unit == 'square_foot':
            result = self.num * 107639
        elif unit == 'square_yard':
            result = self.num * 11959.9
        elif unit == 'square_meter':
            result = self.num * 10000
        elif unit == 'acre':
            result = self.num * 2.47105
        elif unit == 'square_kilometer':
            result = self.num / 100
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "square_kilometer":
                return f"{result} km²"
        else:
            return result


# SquareKilometer
class SquareKilometer:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def square_kilometer_to(self, unit: str) -> Union[float, str]:
        if unit == 'square_centimeter':
            result = self.num * 1e10
        elif unit == 'square_foot':
            result = self.num * 1.076e7
        elif unit == 'square_yard':
            result = self.num * 1.196e6
        elif unit == 'square_meter':
            result = self.num * 1e6
        elif unit == 'acre':
            result = self.num * 247.105
        elif unit == 'hectare':
            result = self.num * 100
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == "square_centimeter":
                return f"{result} cm²"
            elif unit == "square_foot":
                return f"{result} ft²"
            elif unit == "square_yard":
                return f"{result} yd²"
            elif unit == "square_meter":
                return f"{result} m²"
            elif unit == "acre":
                return f"{result} ac"
            elif unit == "hectare":
                return f"{result} ha"
        else:
            return result
