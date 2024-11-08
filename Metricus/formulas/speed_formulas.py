from typing import Union

# Classe base para Velocidade
class Speed:
    def __init__(self, num: float, with_unit: bool) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        return f"{result} {unit}" if self.with_unit else result

# Metros por segundo (m/s)
class MetersPerSecond(Speed):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'km/h':
            result = self.num * 3.6
        elif unit == 'mph':
            result = self.num * 2.23694
        elif unit == 'kn':
            result = self.num * 1.94384
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Quilômetros por hora (km/h)
class KilometersPerHour(Speed):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'm/s':
            result = self.num / 3.6
        elif unit == 'mph':
            result = self.num / 1.60934
        elif unit == 'kn':
            result = self.num / 1.852
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Milhas por hora (mph)
class MilesPerHour(Speed):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'm/s':
            result = self.num / 2.23694
        elif unit == 'km/h':
            result = self.num * 1.60934
        elif unit == 'kn':
            result = self.num / 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)

# Nós (kn)
class Knots(Speed):
    def to(self, unit: str) -> Union[float, str]:
        if unit == 'm/s':
            result = self.num / 1.94384
        elif unit == 'km/h':
            result = self.num * 1.852
        elif unit == 'mph':
            result = self.num * 1.15078
        else:
            raise ValueError("The measurement has an unknown unit")
        return self.format_result(result, unit)