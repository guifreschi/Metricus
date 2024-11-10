from typing import Union

# Classe base para Unidades Elétricas
class ElectricalUnit:
    def __init__(self, num: float, with_unit: bool = False) -> None:
        self.num = num
        self.with_unit = with_unit

    def format_result(self, result: float, unit: str) -> Union[float, str]:
        unit_abbreviations = {
            'ampere': 'A',
            'volt': 'V',
            'ohm': 'Ω',
            'coulomb': 'C',
            'watt': 'W',
            'kilowatt': 'kW',
            'farad': 'F',
            'henry': 'H',
            'siemens': 'S'
        }
        if self.with_unit:
            return f"{result} {unit_abbreviations.get(unit, unit)}"
        else:
            return result

    def raise_value_error(self, parameter: str) -> None:
        raise ValueError(f"{parameter} value needed for conversion.")

# Ampere
class Ampere(ElectricalUnit):
    def ampere_to(self, unit: str, resistance: float = None, voltage: float = None, time: float = None, freq: float = None) -> Union[float, str]:
        result = None

        if unit == 'volt':
            if resistance is not None:
                result = self.num * resistance
            else:
                self.raise_value_error("Resistance")

        elif unit == 'ohm':
            if voltage is not None:
                result = voltage / self.num
            else:
                self.raise_value_error("Voltage")

        elif unit == 'coulomb':
            if time is not None:
                result = self.num * time
            else:
                self.raise_value_error("Time")

        elif unit == 'watt':
            if voltage is not None:
                result = self.num * voltage
            else:
                self.raise_value_error("Voltage")

        elif unit == 'kilowatt':
            if voltage is not None:
                result = (self.num * voltage) / 1000
            else:
                self.raise_value_error("Voltage")

        elif unit == 'henry':
            if voltage is not None and freq is not None:
                result = voltage / (self.num * freq)
            else:
                self.raise_value_error("Voltage and frequency")

        elif unit == 'siemens':
            if resistance is not None:
                result = 1 / resistance
            else:
                self.raise_value_error("Resistance")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Volt
class Volt(ElectricalUnit):
    def volt_to(self, unit: str, resistance: float = None, current: float = None, time: float = None, freq: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if resistance is not None:
                result = self.num / resistance
            else:
                self.raise_value_error("Resistance")

        elif unit == 'ohm':
            if current is not None:
                result = self.num / current
            else:
                self.raise_value_error("Current")

        elif unit == 'coulomb':
            if current is not None and time is not None:
                result = current * time
            else:
                self.raise_value_error("Current and time")

        elif unit == 'watt':
            if current is not None:
                result = self.num * current
            else:
                self.raise_value_error("Current")

        elif unit == 'kilowatt':
            if current is not None:
                result = (self.num * current) / 1000
            else:
                self.raise_value_error("Current")

        elif unit == 'farad':
            if resistance is not None and freq is not None:
                result = 1 / (2 * 3.14159 * resistance * freq)
            else:
                self.raise_value_error("Resistance and frequency")

        elif unit == 'henry':
            if current is not None and freq is not None:
                result = self.num / (2 * 3.14159 * current * freq)
            else:
                self.raise_value_error("Current and frequency")

        elif unit == 'siemens':
            if resistance is not None:
                result = 1 / resistance
            else:
                self.raise_value_error("Resistance")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)


# Ohm
class Ohm(ElectricalUnit):
    def ohm_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, freq: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if voltage is not None:
                result = voltage / self.num
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if current is not None:
                result = self.num * current
            else:
                self.raise_value_error("Current")

        elif unit == 'coulomb':
            if current is not None and time is not None:
                result = current * time
            else:
                self.raise_value_error("Current and time")

        elif unit == 'watt':
            if current is not None:
                result = self.num * (current ** 2)
            else:
                self.raise_value_error("Current")

        elif unit == 'kilowatt':
            if current is not None:
                result = (self.num * (current ** 2)) / 1000
            else:
                self.raise_value_error("Current")

        elif unit == 'farad':
            if freq is not None:
                result = 1 / (2 * 3.14159 * self.num * freq)
            else:
                self.raise_value_error("Frequency")

        elif unit == 'henry':
            if freq is not None:
                result = self.num / (2 * 3.14159 * freq)
            else:
                self.raise_value_error("Frequency")

        elif unit == 'siemens':
            result = 1 / self.num

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Coulomb
class Coulomb(ElectricalUnit):
    def coulomb_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, capacitance: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if time is not None and time != 0:
                result = self.num / time
            else:
                self.raise_value_error("A valid, non-zero time")

        elif unit == 'volt':
            if capacitance is not None and capacitance != 0:
                result = self.num / capacitance
            else:
                self.raise_value_error("A valid, non-zero capacitance")

        elif unit == 'watt':
            if voltage is not None and current is not None:
                result = voltage * current
            else:
                self.raise_value_error("Both voltage and current")

        elif unit in ['ohm', 'kilowatt', 'farad', 'henry', 'siemens']:
            raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Wat
class Watt(ElectricalUnit):
    def watt_to(self, unit: str, current: float = None, voltage: float = None, time: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if voltage is not None:
                result = self.num / voltage
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if current is not None:
                result = self.num / current
            else:
                self.raise_value_error("Current")

        elif unit == 'ohm':
            if current is not None:
                result = self.num / (current ** 2)
            else:
                self.raise_value_error("Current")

        elif unit == 'coulomb':
            if time is not None:
                result = self.num * time
            else:
                self.raise_value_error("Time")

        elif unit == 'kilowatt':
            result = self.num / 1000

        elif unit in ['farad', 'henry', 'siemens']:
            raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Kilowatt 
class Kilowatt(ElectricalUnit):
    def kilowatt_to(self, unit: str, current: float = None, voltage: float = None, time: float = None) -> Union[float, str]:
        result = None

        if unit == 'watt':
            result = self.num * 1000

        elif unit == 'ampere':
            if voltage is not None:
                result = (self.num * 1000) / voltage
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if current is not None:
                result = (self.num * 1000) / current
            else:
                self.raise_value_error("Current")

        elif unit == 'ohm':
            if current is not None:
                result = (self.num * 1000) / (current ** 2)
            else:
                self.raise_value_error("Current")

        elif unit == 'coulomb':
            if time is not None:
                result = (self.num * 1000) * time
            else:
                self.raise_value_error("Time")

        elif unit in ['farad', 'henry', 'siemens']:
            raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Farad 
class Farad(ElectricalUnit):
    def farad_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
        result = None

        if unit == 'coulomb':
            if voltage is not None:
                result = self.num * voltage
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if charge is not None:
                result = charge / self.num
            else:
                self.raise_value_error("Charge")

        elif unit == 'ampere':
            if voltage is not None and time is not None:
                result = self.num * (voltage / time)
            else:
                self.raise_value_error("Voltage and time")

        elif unit == 'ohm':
            if current is not None:
                result = self.num / (current ** 2)
            else:
                self.raise_value_error("Current")

        elif unit in ['watt', 'kilowatt', 'henry', 'siemens']:
            raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)

# Henry 
class Henry(ElectricalUnit):
    def henry_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if voltage is not None:
                result = voltage / self.num
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if current is not None:
                result = self.num * current
            else:
                self.raise_value_error("Current")

        elif unit == 'ohm':
            if time is not None:
                result = self.num / time
            else:
                self.raise_value_error("Time")

        elif unit == 'coulomb':
            if voltage is not None and time is not None:
                result = (voltage * time) / self.num
            else:
                self.raise_value_error("Voltage and time")

        elif unit == 'watt':
            if current is not None:
                result = self.num * (current ** 2)
            else:
                self.raise_value_error("Current")

        elif unit == 'kilowatt':
            if current is not None:
                result = (self.num * (current ** 2)) / 1000
            else:
                self.raise_value_error("Current")

        elif unit in ['farad', 'siemens']:
            raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)


# Siemens 
class Siemens(ElectricalUnit):
    def siemens_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
        result = None

        if unit == 'ampere':
            if voltage is not None:
                result = voltage * self.num
            else:
                self.raise_value_error("Voltage")

        elif unit == 'volt':
            if current is not None:
                result = current / self.num
            else:
                self.raise_value_error("Current")

        elif unit == 'ohm':
            result = 1 / self.num

        elif unit == 'coulomb':
            if current is not None and time is not None:
                result = current * time
            else:
                self.raise_value_error("Current and time")

        elif unit == 'watt':
            if current is not None and voltage is not None:
                result = voltage * current
            else:
                self.raise_value_error("Voltage and current")

        elif unit == 'kilowatt':
            if current is not None and voltage is not None:
                result = (voltage * current) / 1000
            else:
                self.raise_value_error("Voltage and current")

        elif unit == 'farad':
            raise NotImplementedError("Conversion to farad is not supported yet.")

        elif unit == 'henry':
            raise NotImplementedError("Conversion to henry is not supported yet.")

        if result is None:
            raise ValueError("Invalid or unsupported unit provided.")

        return self.format_result(result, unit)
