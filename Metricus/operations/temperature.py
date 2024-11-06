from formulas import temperatures_formulas as tf

unit_list = ['celsius', 'fahrenheit', 'kelvin', 'rankine']

def temperature_converter(temp: float, from_unit: str, to_unit: str) -> str:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")
    else:
        if from_unit.lower() == 'celsius':
            return tf.Celsius(temp).celsius_to(to_unit)
        elif from_unit.lower() == 'fahrenheit':
            return tf.Fahrenheit(temp).fahrenheit_to(to_unit)
        elif from_unit.lower() == 'kelvin':
            return tf.Kelvin(temp).kelvin_to(to_unit)
        elif from_unit.lower() == 'rankine':
            return tf.Rankine(temp).rankine_to(to_unit)
        else:
            raise ValueError("The measurement has an unknown unit")

