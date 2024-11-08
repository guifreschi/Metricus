from typing import Union

# Ampere
class Ampere:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def ampere_to(self, unit: str, resistance: float = None, voltage: float = None, time: float = None, freq: float = None) -> Union[float, str]:
    result = None

    if unit == 'volt':
      if resistance is not None:
        result = self.num * resistance 
      else:
        raise ValueError("Resistance value needed for volt conversion.")
    
    elif unit == 'ohm':
      if voltage is not None:
        result = voltage / self.num  
      else:
        raise ValueError("Voltage value needed for ohm conversion.")
    
    elif unit == 'coulomb':
      if time is not None:
        result = self.num * time  
      else:
        raise ValueError("Time value needed for coulomb conversion.")
    
    elif unit == 'watt':
      if voltage is not None:
        result = self.num * voltage 
      else:
        raise ValueError("Voltage value needed for watt conversion.")
    
    elif unit == 'kilowatt':
      if voltage is not None:
        result = (self.num * voltage) / 1000  
      else:
        raise ValueError("Voltage value needed for kilowatt conversion.")
    
    elif unit == 'farad':
      raise ValueError("Cannot calculate farad directly from ampere without additional parameters.")
    
    elif unit == 'henry':
      if voltage is not None and freq is not None:
        result = voltage / (self.num * freq) 
      else:
        raise ValueError("Voltage and frequency values needed for henry conversion.")
    
    elif unit == 'siemens':
      if resistance is not None:
        result = 1 / resistance  
      else:
        raise ValueError("Resistance value needed for siemens conversion.")
    
    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'volt':
          return f"{result} V"
      elif unit == 'ohm':
          return f"{result} Ω"
      elif unit == 'coulomb':
          return f"{result} C"
      elif unit == 'watt':
          return f"{result} W"
      elif unit == 'kilowatt':
          return f"{result} kW"
      elif unit == 'farad':
          return f"{result} F"
      elif unit == 'henry':
          return f"{result} H"
      elif unit == 'siemens':
          return f"{result} S"
    else:
        return result

# Volt 
class Volt:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def volt_to(self, unit: str, resistance: float = None, current: float = None, time: float = None, freq: float = None) -> Union[float, str]:
    result = None

    if unit == 'ampere':
      if resistance is not None:
        result = self.num / resistance 
      else:
        raise ValueError("Resistance value is needed for ampere conversion.")

    elif unit == 'ohm':
      if current is not None:
        result = self.num / current  
      else:
        raise ValueError("Current value is needed for ohm conversion.")

    elif unit == 'coulomb':
      if current is not None and time is not None:
        result = current * time  
      else:
        raise ValueError("Current and time values are needed for coulomb conversion.")

    elif unit == 'watt':
      if current is not None:
        result = self.num * current 
      else:
        raise ValueError("Current value is needed for watt conversion.")

    elif unit == 'kilowatt':
      if current is not None:
        result = (self.num * current) / 1000  
      else:
        raise ValueError("Current value is needed for kilowatt conversion.")

    elif unit == 'farad':
      if resistance is not None and freq is not None:
        result = 1 / (2 * 3.14159 * resistance * freq) 
      else:
        raise ValueError("Resistance and frequency values are needed for farad conversion.")

    elif unit == 'henry':
      if current is not None and freq is not None:
        result = self.num / (2 * 3.14159 * current * freq)  
      else:
        raise ValueError("Current and frequency values are needed for henry conversion.")

    elif unit == 'siemens':
      if resistance is not None:
        result = 1 / resistance  
      else:
        raise ValueError("Resistance value is needed for siemens conversion.")

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'ampere':
        return f"{result} A"
      elif unit == 'ohm':
        return f"{result} Ω"
      elif unit == 'coulomb':
        return f"{result} C"
      elif unit == 'watt':
        return f"{result} W"
      elif unit == 'kilowatt':
        return f"{result} kW"
      elif unit == 'farad':
        return f"{result} F"
      elif unit == 'henry':
        return f"{result} H"
      elif unit == 'siemens':
        return f"{result} S"
    else:
      return result

# Ohm 
class Ohm:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def ohm_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, freq: float = None) -> Union[float, str]:
    result = None

    if unit == 'ampere':
      if voltage is not None:
        result = voltage / self.num  
      else:
        raise ValueError("Voltage value is needed for ampere conversion.")

    elif unit == 'volt':
      if current is not None:
        result = self.num * current  
      else:
        raise ValueError("Current value is needed for volt conversion.")

    elif unit == 'coulomb':
      if current is not None and time is not None:
        result = current * time  
      else:
        raise ValueError("Current and time values are needed for coulomb conversion.")

    elif unit == 'watt':
      if current is not None:
        result = (self.num * (current ** 2))  
      else:
        raise ValueError("Current value is needed for watt conversion.")

    elif unit == 'kilowatt':
      if current is not None:
        result = (self.num * (current ** 2)) / 1000  
      else:
        raise ValueError("Current value is needed for kilowatt conversion.")

    elif unit == 'farad':
      if freq is not None:
        result = 1 / (2 * 3.14159 * self.num * freq) 
      else:
        raise ValueError("Frequency value is needed for farad conversion.")

    elif unit == 'henry':
      if freq is not None:
        result = self.num / (2 * 3.14159 * freq)  
      else:
        raise ValueError("Frequency value is needed for henry conversion.")

    elif unit == 'siemens':
      result = 1 / self.num  

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'ampere':
        return f"{result} A"
      elif unit == 'volt':
        return f"{result} V"
      elif unit == 'coulomb':
        return f"{result} C"
      elif unit == 'watt':
        return f"{result} W"
      elif unit == 'kilowatt':
        return f"{result} kW"
      elif unit == 'farad':
        return f"{result} F"
      elif unit == 'henry':
        return f"{result} H"
      elif unit == 'siemens':
        return f"{result} S"
    else:
      return result

# Coulomb 
class Coulomb:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def coulomb_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, capacitance: float = None) -> Union[float, str]:
    result = None

    if unit == 'ampere':
      if time is not None and time != 0:
        result = self.num / time  
      else:
        raise ValueError("A valid, non-zero time value is needed for ampere conversion.")

    elif unit == 'volt':
      if capacitance is not None and capacitance != 0:
        result = self.num / capacitance  
      else:
        raise ValueError("A valid, non-zero capacitance value is needed for volt conversion.")

    elif unit == 'watt':
      if voltage is not None and current is not None:
        result = voltage * current  
      else:
        raise ValueError("Both voltage and current values are needed for watt conversion.")

    elif unit in ['ohm', 'kilowatt', 'farad', 'henry', 'siemens']:
      raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'ampere':
        return f"{result} A"
      elif unit == 'volt':
        return f"{result} V"
      elif unit == 'watt':
        return f"{result} W"
      else:
        return result
    else:
        return result

# Watt 
class Watt:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def watt_to(self, unit: str, current: float = None, voltage: float = None, time: float = None) -> Union[float, str]:
    result = None
    
    if unit == 'ampere':
      if voltage is not None:
        result = self.num / voltage  
      else:
        raise ValueError("Voltage is required for conversion to ampere.")

    elif unit == 'volt':
      if current is not None:
        result = self.num / current 
      else:
        raise ValueError("Current is required for conversion to volt.")
    
    elif unit == 'ohm':
      if current is not None:
        result = self.num / (current ** 2)  
      else:
        raise ValueError("Current is required for conversion to ohm.")
    
    elif unit == 'coulomb':
      if time is not None:
        result = self.num * time  
      else:
        raise ValueError("Time is required for conversion to coulomb.")
    
    elif unit == 'kilowatt':
      result = self.num / 1000  
    
    elif unit in ['farad', 'henry', 'siemens']:
      raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")
    
    if self.with_unit:
      if unit == 'ampere':
        return f"{result} A"
      elif unit == 'volt':
          return f"{result} V"
      elif unit == 'ohm':
          return f"{result} Ω"
      elif unit == 'coulomb':
          return f"{result} C"
      elif unit == 'kilowatt':
          return f"{result} kW"
      else:
          return result
    else:
        return result

# Kilowatt 
class Kilowatt:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def kilowatt_to(self, unit: str, current: float = None, voltage: float = None, time: float = None) -> Union[float, str]:
    result = None
    
    if unit == 'watt':
      result = self.num * 1000
    
    elif unit == 'ampere':
      if voltage is not None:
        result = (self.num * 1000) / voltage 
      else:
        raise ValueError("Voltage is required for conversion to ampere.")
    
    elif unit == 'volt':
      if current is not None:
        result = (self.num * 1000) / current  
      else:
        raise ValueError("Current is required for conversion to volt.")
    
    elif unit == 'ohm':
      if current is not None:
        result = (self.num * 1000) / (current ** 2)  
      else:
        raise ValueError("Current is required for conversion to ohm.")
    
    elif unit == 'coulomb':
      if time is not None:
        result = (self.num * 1000) * time  
      else:
        raise ValueError("Time is required for conversion to coulomb.")
    
    elif unit in ['farad', 'henry', 'siemens']:
      raise NotImplementedError(f"Conversion to {unit} is not supported yet.")
    
    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")
    
    if self.with_unit:
      if unit == 'watt':
          return f"{result} W"
      elif unit == 'ampere':
          return f"{result} A"
      elif unit == 'volt':
          return f"{result} V"
      elif unit == 'ohm':
          return f"{result} Ω"
      elif unit == 'coulomb':
          return f"{result} C"
      else:
          return result
    else:
      return result


# Farad
class Farad:
  def __init__(self, num: float, with_unit: bool) -> None:
    self.num = num
    self.with_unit = with_unit

  def farad_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
    result = None


    if unit == 'coulomb':
      if voltage is not None:
        result = self.num * voltage 
      else:
        raise ValueError("Voltage is required for conversion to coulomb.")
    
    # Convertendo para volt (V)
    elif unit == 'volt':
      if charge is not None:
        result = charge / self.num  
      else:
        raise ValueError("Charge is required for conversion to volt.")
    
    elif unit == 'ampere':
      if time is not None:
        result = self.num * (voltage / time) 
      else:
        raise ValueError("Time is required for conversion to ampere.")
    
    elif unit == 'ohm':
      if current is not None:
        result = self.num / (current ** 2) 
      else:
        raise ValueError("Current is required for conversion to ohm.")
    
    elif unit in ['watt', 'kilowatt', 'henry', 'siemens']:
      raise NotImplementedError(f"Conversion to {unit} is not supported yet.")
    
    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")
    
    if self.with_unit:
      if unit == 'coulomb':
        return f"{result} C"
      elif unit == 'volt':
        return f"{result} V"
      elif unit == 'ampere':
        return f"{result} A"
      elif unit == 'ohm':
        return f"{result} Ω"
      else:
        return result
    else:
      return result

# Henry 
class Henry:
  def __init__(self, num: float, with_unit: bool) -> None:
      self.num = num
      self.with_unit = with_unit

  def henry_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
    result = None

    if unit == 'ampere':
      if voltage is not None:
        result = voltage / self.num
      else:
        raise ValueError("Voltage is required for conversion to ampere.")

    elif unit == 'volt':
      if current is not None:
        result = self.num * current
      else:
        raise ValueError("Current is required for conversion to volt.")

    elif unit == 'ohm':
      if time is not None:
        result = self.num / time
      else:
        raise ValueError("Time is required for conversion to ohm.")

    elif unit == 'coulomb':
      if voltage is not None and time is not None:
        result = (voltage * time) / self.num
      else:
        raise ValueError("Voltage and time are required for conversion to coulomb.")

    elif unit == 'watt':
      if current is not None:
        result = self.num * (current ** 2)
      else:
        raise ValueError("Current is required for conversion to watt.")

    elif unit == 'kilowatt':
      if current is not None:
        result = (self.num * (current ** 2)) / 1000
      else:
        raise ValueError("Current is required for conversion to kilowatt.")

    elif unit in ['farad', 'siemens']:
      raise NotImplementedError(f"Conversion to {unit} is not supported yet.")

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'ampere':
        return f"{result} A"
      elif unit == 'volt':
        return f"{result} V"
      elif unit == 'ohm':
        return f"{result} Ω"
      elif unit == 'coulomb':
        return f"{result} C"
      elif unit == 'watt':
        return f"{result} W"
      elif unit == 'kilowatt':
        return f"{result} kW"
    else:
      return result

# Siemens 
class Siemens:
  def __init__(self, num: float, with_unit: bool) -> None:
      self.num = num
      self.with_unit = with_unit

  def siemens_to(self, unit: str, current: float = None, voltage: float = None, time: float = None, charge: float = None) -> Union[float, str]:
    result = None

    if unit == 'ampere':
      if voltage is not None:
        result = voltage * self.num
      else:
        raise ValueError("Voltage is required for conversion to ampere.")

    elif unit == 'volt':
      if current is not None:
        result = current / self.num
      else:
        raise ValueError("Current is required for conversion to volt.")

    elif unit == 'ohm':
      result = 1 / self.num

    elif unit == 'coulomb':
      if current is not None and time is not None:
        result = current * time
      else:
        raise ValueError("Current and time are required for conversion to coulomb.")

    elif unit == 'watt':
      if current is not None and voltage is not None:
        result = voltage * current
      else:
        raise ValueError("Voltage and current are required for conversion to watt.")

    elif unit == 'kilowatt':
      if current is not None and voltage is not None:
        result = (voltage * current) / 1000
      else:
        raise ValueError("Voltage and current are required for conversion to kilowatt.")

    elif unit == 'farad':
      raise NotImplementedError("Conversion to farad is not supported yet.")

    elif unit == 'henry':
      raise NotImplementedError("Conversion to henry is not supported yet.")

    if result is None:
      raise ValueError("Invalid or unsupported unit provided.")

    if self.with_unit:
      if unit == 'ampere':
          return f"{result} A"
      elif unit == 'volt':
          return f"{result} V"
      elif unit == 'ohm':
          return f"{result} Ω"
      elif unit == 'coulomb':
          return f"{result} C"
      elif unit == 'watt':
          return f"{result} W"
      elif unit == 'kilowatt':
          return f"{result} kW"
    else:
        return result
