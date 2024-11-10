from typing import Union

# Classe base para Área
class Area:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        units_map = {
            "square_centimeter": "cm²",
            "square_foot": "ft²",
            "square_meter": "m²",
            "square_yard": "yd²",
            "acre": "ac",
            "hectare": "ha",
            "square_kilometer": "km²",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result

# Square Centimeter (cm²)
class SquareCentimeter(Area):
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
        return self.format_result(result, unit)

# Square Foot (ft²)
class SquareFoot(Area):
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
        return self.format_result(result, unit)

# Square Yard 
class SquareYard(Area):
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
        return self.format_result(result, unit)



# Square Meter (m²)
class SquareMeter(Area):
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
        return self.format_result(result, unit)

# Acre (ac)
class Acre(Area):
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
        return self.format_result(result, unit)

# Hectare (ha)
class Hectare(Area):
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
        return self.format_result(result, unit)

# Square Kilometer (km²)
class SquareKilometer(Area):
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
        return self.format_result(result, unit)
