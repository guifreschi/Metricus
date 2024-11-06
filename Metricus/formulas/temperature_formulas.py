# Celsius
class Celsius:
    def __init__(self, num: float) -> None:
        self.num = num

    def celsius_to(self, unit: str) -> str:
        if unit == 'kelvin':
            result = str(self.num + 273.15) + ' °K'
        elif unit == 'fahrenheit':
            result = str((self.num * 9 / 5) + 32) + ' °F'
        elif unit == 'rankine':
            result = str((self.num * 9 / 5) + 491.67) + ' °R'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Fahrenheit
class Fahrenheit:
    def __init__(self, num: float) -> None:
        self.num = num

    def fahrenheit_to(self, unit: str) -> str:
        if unit == 'celsius':
            result = str((self.num - 32) * 5 / 9) + '°C'
        elif unit == 'kelvin':
            result = str((self.num - 32) * 5 / 9 + 273.15) + '°K'
        elif unit == 'rankine':
            result = str(self.num + 459.67) + '°R'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result


# Kelvin
class Kelvin:
    def __init__(self, num: float) -> None:
        self.num = num

    def kelvin_to(self, unit: str) -> str:
        if unit == 'fahrenheit':
            result = str((self.num - 273.15) * 9 / 5 + 32) + ' °F'
        elif unit == 'celsius':
            result = str(self.num - 273.15) + ' °C'
        elif unit == 'rankine':
            result = str(self.num * 9 / 5) + ' °R'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result

# Rankine
class Rankine:
    def __init__(self, num: float) -> None:
        self.num = num

    def rankine_to(self, unit: str) -> str:
        if unit == 'celsius':
            result = str((self.num - 491.67) * 5 / 9) + ' °C'
        elif unit == 'kelvin':
            result = str(self.num * 5 / 9) + ' °K'
        elif unit == 'fahrenheit':
            result = str(self.num - 459.67) + ' °F'
        else:
            raise ValueError("The measurement has an unknown unit")
        return result
