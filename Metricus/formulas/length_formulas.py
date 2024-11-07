from typing import Union

# Millimeter
class Millimeter:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def millimeter_to(self, unit: str) -> Union[float, str]:
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
        
        if self.with_unit:
            if unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"   
        else:
            return result

# Centimeter
class Centimeter:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def centimeter_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result

# Inch
class Inch:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def inch_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result

# Foot
class Foot:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def foot_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result
        
# Yard
class Yard:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def yard_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result


# Meter
class Meter:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def meter_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result

# Kilometer
class Kilometer:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def kilometer_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'mile':
                return f"{result} mi"
            elif unit == "nautical_mile":
                return f"{result} NM"
        else:
            return result

# Mile
class Mile:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def mile_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'nautical_mile':
                return f"{result} NM"
        else:
            return result

# Nautical Mile
class NauticalMile:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def nautical_mile_to(self, unit: str) -> Union[float, str]:
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

        if self.with_unit:
            if unit == 'millimeter':
                return f"{result} mm"
            elif unit == 'centimeter':
                return f"{result} cm"
            elif unit == 'inch':
                return f"{result} in"
            elif unit == 'foot':
                return f"{result} ft"
            elif unit == 'yard':
                return f"{result} yd"
            elif unit == 'meter':
                return f"{result} m"
            elif unit == 'kilometer':
                return f"{result} km"
            elif unit == 'mile':
                return f"{result} mi"
        else:
            return result
