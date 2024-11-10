from typing import Union


# Classe base para unidades de temperatura
class TemperatureUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        units_map = {
            "celsius": "°C",
            "fahrenheit": "°F",
            "kelvin": "°K",
            "rankine": "°R",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result


# Celsius
class Celsius(TemperatureUnit):
    def celsius_to(self, unit: str) -> Union[float, str]:
        if unit == 'kelvin':
            result = self.num + 273.15
        elif unit == 'fahrenheit':
            result = (self.num * 9 / 5) + 32
        elif unit == 'rankine':
            result = (self.num * 9 / 5) + 491.67
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Fahrenheit
class Fahrenheit(TemperatureUnit):
    def fahrenheit_to(self, unit: str) -> Union[float, str]:
        if unit == 'celsius':
            result = (self.num - 32) * 5 / 9
        elif unit == 'kelvin':
            result = (self.num - 32) * 5 / 9 + 273.15
        elif unit == 'rankine':
            result = self.num + 459.67
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Kelvin
class Kelvin(TemperatureUnit):
    def kelvin_to(self, unit: str) -> Union[float, str]:
        if unit == 'fahrenheit':
            result = (self.num - 273.15) * 9 / 5 + 32
        elif unit == 'celsius':
            result = self.num - 273.15
        elif unit == 'rankine':
            result = self.num * 9 / 5
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)


# Rankine
class Rankine(TemperatureUnit):
    def rankine_to(self, unit: str) -> Union[float, str]:
        if unit == 'celsius':
            result = (self.num - 491.67) * 5 / 9
        elif unit == 'kelvin':
            result = self.num * 5 / 9
        elif unit == 'fahrenheit':
            result = self.num - 459.67
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)
