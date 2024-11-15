from formulas import electricity_formulas as ef
from typing import Union

unit_list = ['ampere', 'volt', 'ohm', 'coulomb', 'watt', 'kilowatt', 'farad', 'henry', 'siemens']

def electricity_converter(
    value: float, 
    from_unit: str, 
    to_unit: str, 
    resistance: float = None, 
    current: float = None, 
    voltage: float = None, 
    time: float = None, 
    freq: float = None, 
    with_unit: bool = False
) -> Union[float, str]:
    if from_unit not in unit_list or to_unit not in unit_list:
        raise ValueError("The measurement has an unknown unit")

    if from_unit == 'ampere':
        return ef.Ampere(value, with_unit=with_unit).ampere_to(
            to_unit, resistance=resistance, voltage=voltage, time=time, freq=freq
        )
    elif from_unit == 'volt':
        return ef.Volt(value, with_unit=with_unit).volt_to(
            to_unit, resistance=resistance, current=current, time=time, freq=freq
        )
    elif from_unit == 'ohm':
        return ef.Ohm(value, with_unit=with_unit).ohm_to(
            to_unit, voltage=voltage, current=current
        )
    elif from_unit == 'coulomb':
        return ef.Coulomb(value, with_unit=with_unit).coulomb_to(
            to_unit, current=current, time=time
        )
    elif from_unit == 'watt':
        return ef.Watt(value, with_unit=with_unit).watt_to(
            to_unit, voltage=voltage, current=current
        )
    elif from_unit == 'kilowatt':
        return ef.Kilowatt(value, with_unit=with_unit).kilowatt_to(
            to_unit, voltage=voltage, current=current
        )
    elif from_unit == 'farad':
        return ef.Farad(value, with_unit=with_unit).farad_to(
            to_unit, resistance=resistance, freq=freq
        )
    elif from_unit == 'henry':
        return ef.Henry(value, with_unit=with_unit).henry_to(
            to_unit, current=current, freq=freq
        )
    elif from_unit == 'siemens':
        return ef.Siemens(value, with_unit=with_unit).siemens_to(
            to_unit, resistance=resistance
        )
    else:
        raise ValueError("The measurement has an unknown unit")
