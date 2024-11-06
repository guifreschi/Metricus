from formulas import temperature_formulas as tf
from typing import Union

unit_list = ['celsius', 'fahrenheit', 'kelvin', 'rankine']

def temperature_converter(temp: float, from_unit: str, to_unit: str, with_unit: bool = False) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit == 'celsius':
            return tf.Celsius(temp, with_unit=with_unit).celsius_to(to_unit)
        elif from_unit == 'fahrenheit':
            return tf.Fahrenheit(temp, with_unit=with_unit).fahrenheit_to(to_unit)
        elif from_unit == 'kelvin':
            return tf.Kelvin(temp, with_unit=with_unit).kelvin_to(to_unit)
        elif from_unit == 'rankine':
            return tf.Rankine(temp, with_unit=with_unit).rankine_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")

temp = temperature_converter(25, 'fahrenheit', 'kelvin', with_unit=True) 
print(temp)