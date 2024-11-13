from typing import Union

# Base class for length units
class LengthUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        """
        Initialize a length unit instance.
        :param num: The numerical value of the length.
        :param with_unit: Flag to include unit in the formatted result.
        """
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        """
        Format the result with or without unit.
        :param result: The calculated length.
        :param unit: The unit of the result.
        :return: Formatted length with or without unit.
        """
        units_map = {
            "millimeter": "mm",
            "centimeter": "cm",
            "inch": "in",
            "foot": "ft",
            "yard": "yd",
            "meter": "m",
            "kilometer": "km",
            "mile": "mi",
            "nautical_mile": "NM",
        }
        return f"{result} {units_map[unit]}" if self.with_unit else result

# Millimeter 
class Millimeter(LengthUnit):
    def millimeter_to(self, unit: str) -> Union[float, str]:
        """
        Convert millimeters to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'centimeter':
            result = self.num / 10
        elif unit == 'inch':
            result = self.num / 25.4
        elif unit == 'foot':
            result = self.num / 304.8
        elif unit == 'yard':
            result = self.num / 914.4
        elif unit == 'meter':
            result = self.num / 1000
        elif unit == 'kilometer':
            result = self.num / 1_000_000
        elif unit == 'mile':
            result = self.num / 1_609_344
        elif unit == 'nautical_mile':
            result = self.num / 1_852_000
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Centimeter 
class Centimeter(LengthUnit):
    def centimeter_to(self, unit: str) -> Union[float, str]:
        """
        Convert centimeters to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 10
        elif unit == 'inch':
            result = self.num / 2.54
        elif unit == 'foot':
            result = self.num / 30.48
        elif unit == 'yard':
            result = self.num / 91.44
        elif unit == 'meter':
            result = self.num / 100
        elif unit == 'kilometer':
            result = self.num / 100_000
        elif unit == 'mile':
            result = self.num / 160_934
        elif unit == 'nautical_mile':
            result = self.num / 185200
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)

# Inch 
class Inch(LengthUnit):
    def inch_to(self, unit: str) -> Union[float, str]:
        """
        Convert inches to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 25.4
        elif unit == 'centimeter':
            result = self.num * 2.54
        elif unit == 'foot':
            result = self.num / 12
        elif unit == 'yard':
            result = self.num / 36
        elif unit == 'meter':
            result = self.num / 39.3701
        elif unit == 'kilometer':
            result = self.num / 39_370.1
        elif unit == 'mile':
            result = self.num / 63_360
        elif unit == 'nautical_mile':
            result = self.num / 73057.3
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)

# Foot 
class Foot(LengthUnit):
    def foot_to(self, unit: str) -> Union[float, str]:
        """
        Convert feet to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 304.8
        elif unit == 'centimeter':
            result = self.num * 30.48
        elif unit == 'inch':
            result = self.num * 12
        elif unit == 'yard':
            result = self.num / 3
        elif unit == 'meter':
            result = self.num / 3.28084
        elif unit == 'kilometer':
            result = self.num / 3280.84
        elif unit == 'mile':
            result = self.num / 5280
        elif unit == 'nautical_mile':
            result = self.num / 6076.12
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Yard 
class Yard(LengthUnit):
    def yard_to(self, unit: str) -> Union[float, str]:
        """
        Convert yards to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 914.4
        elif unit == 'centimeter':
            result = self.num * 91.44
        elif unit == 'inch':
            result = self.num * 36
        elif unit == 'foot':
            result = self.num * 3
        elif unit == 'meter':
            result = self.num * 0.9144
        elif unit == 'kilometer':
            result = self.num * 0.0009144
        elif unit == 'mile':
            result = self.num * 0.000568182
        elif unit == 'nautical_mile':
            result = self.num * 0.000493737
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)

# Meter 
class Meter(LengthUnit):
    def meter_to(self, unit: str) -> Union[float, str]:
        """
        Convert meters to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 1000
        elif unit == 'centimeter':
            result = self.num * 100
        elif unit == 'inch':
            result = self.num * 39.3701
        elif unit == 'foot':
            result = self.num * 3.28084
        elif unit == 'yard':
            result = self.num / 0.9144
        elif unit == 'kilometer':
            result = self.num / 1000
        elif unit == 'mile':
            result = self.num / 1609.34
        elif unit == 'nautical_mile':
            result = self.num / 1852
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)

# Kilometer 
class Kilometer(LengthUnit):
    def kilometer_to(self, unit: str) -> Union[float, str]:
        """
        Convert kilometers to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 1_000_000
        elif unit == 'centimeter':
            result = self.num * 100_000
        elif unit == 'inch':
            result = self.num * 39_370.1
        elif unit == 'foot':
            result = self.num * 3280.84
        elif unit == 'yard':
            result = self.num * 1093.61
        elif unit == 'meter':
            result = self.num * 1000
        elif unit == 'mile':
            result = self.num / 1.60934
        elif unit == 'nautical_mile':
            result = self.num / 1.852
        else:
            raise ValueError("The measurement has an unknown unit")
        
        return self.format_result(result, unit)

# Mile
class Mile(LengthUnit):
    def mile_to(self, unit: str) -> Union[float, str]:
        """
        Convert miles to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 1_609_344
        elif unit == 'centimeter':
            result = self.num * 160_934
        elif unit == 'inch':
            result = self.num * 63_360
        elif unit == 'foot':
            result = self.num * 5280
        elif unit == 'yard':
            result = self.num * 1_760
        elif unit == 'meter':
            result = self.num * 1609.34
        elif unit == 'kilometer':
            result = self.num * 1.60934
        elif unit == 'nautical_mile':
            result = self.num * 0.868976
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)

# Nautical Mile
class NauticalMile(LengthUnit):
    def nautical_mile_to(self, unit: str) -> Union[float, str]:
        """
        Convert nautical miles to the specified unit.
        :param unit: The unit to convert to.
        :return: Converted length.
        """
        if unit == 'millimeter':
            result = self.num * 1_852_000
        elif unit == 'centimeter':
            result = self.num * 185_200
        elif unit == 'inch':
            result = self.num * 72_928.8
        elif unit == 'foot':
            result = self.num * 6076.12
        elif unit == 'yard':
            result = self.num * 2025.37
        elif unit == 'meter':
            result = self.num * 1852
        elif unit == 'kilometer':
            result = self.num * 1.852
        elif unit == 'mile':
            result = self.num * 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")

        return self.format_result(result, unit)
