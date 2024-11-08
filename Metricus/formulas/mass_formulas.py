from typing import Union

# Milligram
class Milligram:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result
    
# Carat
class Carat:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
    
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result

# Gram
class Gram:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result
    
# Ounce
class Ounce:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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

        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result 
    
# Pound
class Pound:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result 
    
# Kilogram
class Kilogram:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'stone':
                return f"{result} st"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result 

# Stone
class Stone:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'slug':
               return f"{result} sl"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result 
   
# Slug
class Slug:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
               return f"{result} st"
            elif unit == 'tonne':
                return f"{result} t"
        else:
            return result 

# Tonne
class Tonne:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

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
        
        if self.with_unit:
            if unit == 'milligram':
                return f"{result} mg"
            elif unit == 'carat':
                return f"{result} ct"
            elif unit == 'gram':
                return f"{result} g"
            elif unit == 'ounce':
                return f"{result} oz"
            elif unit == 'pound':
                return f"{result} lb"
            elif unit == 'kilogram':
                return f"{result} kg"
            elif unit == 'stone':
               return f"{result} st"
            elif unit == 'slug':
                return f"{result} sl"
        else:
            return result 
