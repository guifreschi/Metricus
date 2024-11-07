class Millimeter:
    def __init__(self, num: float) -> None:
        self.num = num

    def millimeter_to(self, unit: str) -> str:
        if unit == 'centimeter':
            result = str(self.num / 10) + ' cm'
        elif unit == 'inch':
            result = str(self.num / 25.4) + ' in'
        elif unit == 'foot':
            result = str(self.num / 304.8) + ' ft'
        elif unit == 'meter':
            result = str(self.num / 1000) + ' m'
        elif unit == 'kilometer':
            result = str(self.num / 1_000_000) + ' km'
        elif unit == 'mile':
            result = str(self.num / 1_609_344) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 1_852_000) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Centimeter
class Centimeter:
    def __init__(self, num: float) -> None:
        self.num = num

    def centimeter_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 10) + ' mm'
        elif unit == 'inch':
            result = str(self.num / 2.54) + ' in'
        elif unit == 'foot':
            result = str(self.num / 30.48) + ' ft'
        elif unit == 'meter':
            result = str(self.num / 100) + ' m'
        elif unit == 'kilometer':
            result = str(self.num / 100_000) + ' km'
        elif unit == 'mile':
            result = str(self.num / 160_934) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 185200) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Inch
class Inch:
    def __init__(self, num: float) -> None:
        self.num = num

    def inch_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 25.4) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 2.54) + ' cm'
        elif unit == 'foot':
            result = str(self.num / 12) + ' ft'
        elif unit == 'meter':
            result = str(self.num / 39.3701) + ' m'
        elif unit == 'kilometer':
            result = str(self.num / 39_370.1) + ' km'
        elif unit == 'mile':
            result = str(self.num / 63_360) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 73057.3) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Foot
class Foot:
    def __init__(self, num: float) -> None:
        self.num = num

    def foot_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 304.8) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 30.48) + ' cm'
        elif unit == 'inch':
            result = str(self.num * 12) + ' in'
        elif unit == 'meter':
            result = str(self.num / 3.28084) + ' m'
        elif unit == 'kilometer':
            result = str(self.num / 3280.84) + ' km'
        elif unit == 'mile':
            result = str(self.num / 5280) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 6076.12) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Meter
class Meter:
    def __init__(self, num: float) -> None:
        self.num = num

    def meter_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 1000) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 100) + ' cm'
        elif unit == 'inch':
            result = str(self.num * 39.3701) + ' in'
        elif unit == 'foot':
            result = str(self.num * 3.28084) + ' ft'
        elif unit == 'kilometer':
            result = str(self.num / 1000) + ' km'
        elif unit == 'mile':
            result = str(self.num / 1609.34) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 1852) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Kilometer
class Kilometer:
    def __init__(self, num: float) -> None:
        self.num = num

    def kilometer_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 1_000_000) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 100_000) + ' cm'
        elif unit == 'inch':
            result = str(self.num * 39_370.1) + ' in'
        elif unit == 'foot':
            result = str(self.num * 3280.84) + ' ft'
        elif unit == 'meter':
            result = str(self.num * 1000) + ' m'
        elif unit == 'mile':
            result = str(self.num / 1.60934) + ' mi'
        elif unit == 'nautical_mile':
            result = str(self.num / 1.852) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Mile
class Mile:
    def __init__(self, num: float) -> None:
        self.num = num

    def mile_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 1_609_344) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 160_934) + ' cm'
        elif unit == 'inch':
            result = str(self.num * 63_360) + ' in'
        elif unit == 'foot':
            result = str(self.num * 5280) + ' ft'
        elif unit == 'meter':
            result = str(self.num * 1609.34) + ' m'
        elif unit == 'kilometer':
            result = str(self.num * 1.60934) + ' km'
        elif unit == 'nautical_mile':
            result = str(self.num * 0.868976) + ' NM'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Nautical Mile
class NauticalMile:
    def __init__(self, num: float) -> None:
        self.num = num

    def nautical_mile_to(self, unit: str) -> str:
        if unit == 'millimeter':
            result = str(self.num * 1_852_000) + ' mm'
        elif unit == 'centimeter':
            result = str(self.num * 185_200) + ' cm'
        elif unit == 'inch':
            result = str(self.num * 72_913.39) + ' in'
        elif unit == 'foot':
            result = str(self.num * 6076.12) + ' ft'
        elif unit == 'meter':
            result = str(self.num * 1852) + ' m'
        elif unit == 'kilometer':
            result = str(self.num * 1.852) + ' km'
        elif unit == 'mile':
            result = str(self.num * 1.15078) + ' mi'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
