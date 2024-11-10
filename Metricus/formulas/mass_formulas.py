from typing import Union

# Classe base para peso
class WeightUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        units_map = {
            "milligram": "mg",
            "carat": "ct",
            "gram": "g",
            "ounce": "oz",
            "pound": "lb",
            "kilogram": "kg",
            "stone": "st",
            "slug": "sl",
            "tonne": "t",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result

# Milligram
class Milligram(WeightUnit):
    def milligram_to(self, unit: str) -> Union[float, str]:
        if unit == 'carat':
            result = self.num / 200
        elif unit == 'gram':
            result = self.num / 1000
        elif unit == 'ounce':
            result = self.num / 28_349.5
        elif unit == 'pound':
            result = self.num / 453_592
        elif unit == 'kilogram':
            result = self.num / 1_000_000
        elif unit == 'stone':
            result = self.num / 6_350_290
        elif unit == 'slug':
            result = self.num / 14_593_900
        elif unit == 'tonne':
            result = self.num / 1_000_000_000
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Carat
class Carat(WeightUnit):
    def carat_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 200
        elif unit == 'gram':
            result = self.num / 5
        elif unit == 'ounce':
            result = self.num / 141.7476
        elif unit == 'pound':
            result = self.num / 2267.96
        elif unit == 'kilogram':
            result = self.num / 5000
        elif unit == 'stone':
            result = self.num / 6350.29
        elif unit == 'slug':
            result = (self.num * 200) / 1_000_000 / 14.5939
        elif unit == 'tonne':
            result = self.num / 5_000_000
        else:
            raise ValueError("The measurement has an unknown unit")
    
        return self.format_result(result, unit)

# Gram
class Gram(WeightUnit):
    def gram_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 1000
        elif unit == 'carat':
            result = self.num * 5
        elif unit == 'ounce':
            result = self.num / 28.3495
        elif unit == 'pound':
            result = self.num / 453.592
        elif unit == 'kilogram':
            result = self.num / 1000
        elif unit == 'stone':
            result = self.num / 6_350.29
        elif unit == 'slug':
            result = self.num / 14_593.9
        elif unit == 'tonne':
            result = self.num / 1_000_000
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Ounce
class Ounce(WeightUnit):
    def ounce_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 28_349.5
        elif unit == 'carat':
            result = self.num * 141.7476
        elif unit == 'gram':
            result = self.num * 28.3495
        elif unit == 'pound':
            result = self.num / 16
        elif unit == 'kilogram':
            result = self.num / 35.274
        elif unit == 'stone':
            result = self.num / 224
        elif unit == 'slug':
            result = self.num / 514.78
        elif unit == 'tonne':
            result = self.num / 35_274.96
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Pound
class Pound(WeightUnit):
    def pound_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 453_592
        elif unit == 'carat':
            result = self.num * 2267.96
        elif unit == 'gram':
            result = self.num * 453.592
        elif unit == 'ounce':
            result = self.num * 16
        elif unit == 'kilogram':
            result = self.num / 2.20462
        elif unit == 'stone':
            result = self.num / 14
        elif unit == 'slug':
            result = self.num / 32.174
        elif unit == 'tonne':
            result = self.num / 2204.62
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Kilogram
class Kilogram(WeightUnit):
    def kilogram_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 1_000_000
        elif unit == 'carat':
            result = self.num * 5000
        elif unit == 'gram':
            result = self.num * 1000
        elif unit == 'ounce':
            result = self.num * 35.274
        elif unit == 'pound':
            result = self.num * 2.20462
        elif unit == 'stone':
            result = self.num / 6.35
        elif unit == 'slug':
            result = self.num / 14.5939
        elif unit == 'tonne':
            result = self.num / 1000
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Stone
class Stone(WeightUnit):
    def stone_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 6_350_290
        elif unit == 'carat':
            result = self.num * 31_751.45
        elif unit == 'gram':
            result = self.num * 6_350.29
        elif unit == 'ounce':
            result = self.num * 224
        elif unit == 'pound':
            result = self.num * 14
        elif unit == 'kilogram':
            result = self.num * 6.35029
        elif unit == 'slug':
            result = self.num * (6.35029 / 14.5939)
        elif unit == 'tonne':
            result = self.num * 0.15747
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Slug
class Slug(WeightUnit):
    def slug_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 14_593_900
        elif unit == 'carat':
            result = self.num * 72_969.5
        elif unit == 'gram':
            result = self.num * 14_593.9
        elif unit == 'ounce':
            result = self.num * 514.78
        elif unit == 'pound':
            result = self.num * 32.174
        elif unit == 'kilogram':
            result = self.num * 14.5939
        elif unit == 'stone':
            result = self.num * (14.5939 / 6.35029)
        elif unit == 'tonne':
            result = self.num * (14.5939 / 1000)
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Tonne
class Tonne(WeightUnit):
    def tonne_to(self, unit: str) -> Union[float, str]:
        if unit == 'milligram':
            result = self.num * 1_000_000_000
        elif unit == 'carat':
            result = self.num * 5_000_000
        elif unit == 'gram':
            result = self.num * 1_000_000
        elif unit == 'ounce':
            result = self.num * 35_274
        elif unit == 'pound':
            result = self.num * 2204.62
        elif unit == 'kilogram':
            result = self.num * 1000
        elif unit == 'stone':
            result = self.num * 157.473
        elif unit == 'slug':
            result = self.num * 68.5218
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)
