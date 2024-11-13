"""
This module provides classes for converting temperature between different units.

Classes:

    - TemperatureUnit: A base class for temperature conversions. It handles the temperature value and whether or not the unit should be included in the output.
    - Celsius: A class for converting temperature from Celsius (°C) to other units such as Kelvin (K), Fahrenheit (°F), and Rankine (°R).

Usage Example:

    # Create a Celsius object
    temp_celsius = Celsius(25, with_unit=True)

    # Convert 25 degrees Celsius to Fahrenheit
    result = temp_celsius.celsius_to('fahrenheit')
    print(result)  # Output: "77.0 °F"
"""


from typing import Union

# Base class for temperature units
class TemperatureUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        """
        Initialize a temperature unit instance.
        :param num: The numerical value of the temperature.
        :param with_unit: Flag to include unit in the formatted result.
        """
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        """
        Format the result with or without unit.
        :param result: The calculated temperature.
        :param unit: The unit of the result.
        :return: Formatted temperature with or without unit.
        """
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
        """
        Convert Celsius to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted temperature.
        """
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
        """
        Convert Fahrenheit to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted temperature.
        """
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
        """
        Convert Kelvin to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted temperature.
        """
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
        """
        Convert Rankine to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted temperature.
        """
        if unit == 'celsius':
            result = (self.num - 491.67) * 5 / 9
        elif unit == 'kelvin':
            result = self.num * 5 / 9
        elif unit == 'fahrenheit':
            result = self.num - 459.67
        else:
            raise ValueError("Unknown unit")

        return self.format_result(result, unit)
