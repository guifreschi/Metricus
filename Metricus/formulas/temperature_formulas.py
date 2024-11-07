from typing import Union

# Celsius
class Celsius:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def celsius_to(self, unit: str) -> Union[float, str]:
        if unit == 'kelvin':
            result = self.num + 273.15
        elif unit == 'fahrenheit':
            result = (self.num * 9 / 5) + 32
        elif unit == 'rankine':
            result = (self.num * 9 / 5) + 491.67
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'kelvin':
                return f"{result} °K"
            elif unit == 'fahrenheit':
                return f"{result} °F"
            elif unit == 'rankine':
                return f"{result} °R"
        else:
            return result

# Fahrenheit
class Fahrenheit:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def fahrenheit_to(self, unit: str) -> Union[float, str]:
        if unit == 'celsius':
            result = (self.num - 32) * 5 / 9
        elif unit == 'kelvin':
            result = (self.num - 32) * 5 / 9 + 273.15
        elif unit == 'rankine':
            result = self.num + 459.67
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'celsius':
                return f"{result} °C"
            elif unit == 'kelvin':
                return f"{result} °K"
            elif unit == 'rankine':
                return f"{result} °R"
        else:
            return result

# Kelvin
class Kelvin:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def kelvin_to(self, unit: str) -> Union[float, str]:
        if unit == 'fahrenheit':
            result = (self.num - 273.15) * 9 / 5 + 32
        elif unit == 'celsius':
            result = self.num - 273.15
        elif unit == 'rankine':
            result = self.num * 9 / 5
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'fahrenheit':
                return f"{result} °F"
            elif unit == 'celsius':
                return f"{result} °C"
            elif unit == 'rankine':
                return f"{result} °R"
        else:
            return result

# Rankine
class Rankine:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def rankine_to(self, unit: str) -> Union[float, str]:
        if unit == 'celsius':
            result = (self.num - 491.67) * 5 / 9
        elif unit == 'kelvin':
            result = self.num * 5 / 9
        elif unit == 'fahrenheit':
            result = self.num - 459.67
        else:
            raise ValueError("The measurement has an unknown unit")
        
        if self.with_unit:
            if unit == 'celsius':
                return f"{result} °C"
            elif unit == 'kelvin':
                return f"{result} °K"
            elif unit == 'fahrenheit':
                return f"{result} °F"
        else:
            return result 
    
