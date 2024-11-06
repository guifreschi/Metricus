# Milligram
class Milligram:
    def __init__(self, num: float) -> None:
        self.num = num

    def milligram_to(self, unit: str) -> str:
        if unit == 'carat':
            result = str(self.num / 200) + ' ct'
        elif unit == 'gram':
            result = str(self.num / 1000) + ' g'
        elif unit == 'ounce':
            result = str(self.num / 28_349.5) + ' oz'
        elif unit == 'pound':
            result = str(self.num / 453_592) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num / 1_000_000) + ' kg'
        elif unit == 'stone':
            result = str(self.num / 6_350_290) + ' st'
        elif unit == 'slug':
            result = str(self.num / 14_593_900) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 1_000_000_000) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
    
# Carat
class Carat:
    def __init__(self, num: float) -> None:
        self.num = num

    def carat_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 200) + ' mg'
        elif unit == 'gram':
            result = str(self.num / 5) + ' g'
        elif unit == 'ounce':
            result = str(self.num / 141.7476) + ' oz'
        elif unit == 'pound':
            result = str(self.num / 2267.96) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num / 5000) + ' kg'
        elif unit == 'stone':
            result = str(self.num / 6350.29) + ' st'
        elif unit == 'slug':
            result = str((self.num * 200) / 1_000_000 / 14.5939) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 5_000_000) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Gram
class Gram:
    def __init__(self, num: float) -> None:
        self.num = num

    def gram_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 1000) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 5) + ' ct'
        elif unit == 'ounce':
            result = str(self.num / 28.3495) + ' oz'
        elif unit == 'pound':
            result = str(self.num / 453.592) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num / 1000) + ' kg'
        elif unit == 'stone':
            result = str(self.num / 6_350.29) + ' st'
        elif unit == 'slug':
            result = str(self.num / 14_593.9) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 1_000_000) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
    
# Ounce
class Ounce:
    def __init__(self, num: float) -> None:
        self.num = num

    def ounce_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 28_349.5) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 141.7476) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 28.3495) + ' g'
        elif unit == 'pound':
            result = str(self.num / 16) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num / 35.274) + ' kg'
        elif unit == 'stone':
            result = str(self.num / 224) + ' st'
        elif unit == 'slug':
            result = str(self.num / 514.78) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 35_274.96) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")

        return result  
    
# Pound
class Pound:
    def __init__(self, num: float) -> None:
        self.num = num

    def pound_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 453_592) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 2267.96) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 453.592) + ' g'
        elif unit == 'ounce':
            result = str(self.num * 16) + ' oz'
        elif unit == 'kilogram':
            result = str(self.num / 2.20462) + ' kg'
        elif unit == 'stone':
            result = str(self.num / 14) + ' st'
        elif unit == 'slug':
            result = str(self.num / 32.174) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 2204.62) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result  
    
# Kilogram
class Kilogram:
    def __init__(self, num: float) -> None:
        self.num = num

    def kilogram_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 1_000_000) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 5000) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 1000) + ' g'
        elif unit == 'ounce':
            result = str(self.num * 35.274) + ' oz'
        elif unit == 'pound':
            result = str(self.num * 2.20462) + ' lb'
        elif unit == 'stone':
            result = str(self.num / 6.35) + ' st'
        elif unit == 'slug':
            result = str(self.num / 14.5939) + ' sl'
        elif unit == 'tonne':
            result = str(self.num / 1000) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Stone
class Stone:
    def __init__(self, num: float) -> None:
        self.num = num

    def stone_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 6_350_290) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 31_751.45) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 6_350.29) + ' g'
        elif unit == 'ounce':
            result = str(self.num * 224) + ' oz'
        elif unit == 'pound':
            result = str(self.num * 14) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num * 6.35029) + ' kg'
        elif unit == 'slug':
            result = str(self.num * (6.35029 / 14.5939)) + ' sl'
        elif unit == 'tonne':
            result = str(self.num * 0.15747) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
   
# Slug
class Slug:
    def __init__(self, num: float) -> None:
        self.num = num

    def slug_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 14_593_900) + ' mg'
        elif unit == 'carat':
            result = str(self.num * (14_593.9 / 0.0002)) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 14_593.9) + ' g'
        elif unit == 'ounce':
            result = str(self.num * 514.78) + ' oz'
        elif unit == 'pound':
            result = str(self.num * 32.174) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num * 14.5939) + ' kg'
        elif unit == 'stone':
            result = str(self.num * (14.5939 / 6.35029)) + ' st'
        elif unit == 'tonne':
            result = str(self.num * (14.5939 / 1000)) + ' t'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Tonne
class Tonne:
    def __init__(self, num: float) -> None:
        self.num = num

    def tonne_to(self, unit: str) -> str:
        if unit == 'milligram':
            result = str(self.num * 1_000_000_000) + ' mg'
        elif unit == 'carat':
            result = str(self.num * 5_000_000) + ' ct'
        elif unit == 'gram':
            result = str(self.num * 1_000_000) + ' g'
        elif unit == 'ounce':
            result = str(self.num * 35_274) + ' oz'
        elif unit == 'pound':
            result = str(self.num * 2204.62) + ' lb'
        elif unit == 'kilogram':
            result = str(self.num * 1000) + ' kg'
        elif unit == 'stone':
            result = str(self.num * 157.473) + ' st'
        elif unit == 'slug':
            result = str(self.num * 68.5218) + ' sl'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
