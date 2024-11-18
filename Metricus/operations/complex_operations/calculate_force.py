"""
This module provides a function to calculate the force based on mass, acceleration, and the desired units for both.

Function:
    - calculate_force: A function that calculates the force by converting the provided mass and acceleration 
      into the correct units and then calculating the resulting force in the specified unit.

Units Supported for Conversion:
    - Mass Units:
        - 'kilogram': Kilogram, the base unit of mass in the metric system.
        - Other mass units can be converted to kilogram using the `mass_converter` function from the `operations.mass` module.
    
    - Acceleration Units:
        - 'meter_per_second_squared': Meter per Second Squared (m/s²), the standard unit for acceleration.
        - Other acceleration units can be converted to meter per second squared using the `acceleration_converter` function from the `operations.acceleration` module.
    
    - Force Units:
        - 'newton': Newton (N), the standard unit of force in the metric system.
        - 'dyne': Dyne, a CGS unit of force.
        - 'kilonewton': Kilonewton (kN), a metric unit of force.
        - 'pound_force': Pound-force (lbf), a unit of force in the imperial system.
        - 'ounce_force': Ounce-force, a unit of force in the imperial system.
        - 'ton_force': Ton-force, a unit of force in the imperial system.
        - 'kilogram_force': Kilogram-force, a unit of force based on the mass of one kilogram.
        - 'gram_force': Gram-force, a unit of force based on the mass of one gram.
        - 'millinewton': Millinewton (mN), a metric unit of force equal to one-thousandth of a newton.
        - 'poundal': Poundal, a unit of force in the imperial system.
        - 'slug_force': Slug-force, a unit of force in the imperial system.

Parameters:
    - mass (float): The mass value to be used in the force calculation.
    - acceleration (float): The acceleration value to be used in the force calculation.
    - force_unit (str, optional): The unit of force to return. Defaults to 'newton'. Supported units include:
      'newton', 'dyne', 'kilonewton', 'pound_force', 'ounce_force', 'ton_force', 'kilogram_force', 
      'gram_force', 'millinewton', 'poundal', 'slug_force'.
    - mass_unit (str, optional): The unit of mass for the provided mass value. Defaults to 'kilogram'. 
      Other units are converted to kilograms.
    - acceleration_unit (str, optional): The unit of acceleration for the provided acceleration value. Defaults to 'meter_per_second_squared'. 
      Other units are converted to meters per second squared.
    - with_unit (bool, optional): If True, returns the result with the unit. Defaults to False, which returns just the numeric value.

Returns:
    - Union[float, str]: The calculated force in the specified unit. The result is returned as a float if `with_unit` is False, 
      or as a string with the unit if `with_unit` is True.

Raises:
    - ValueError: If the specified force unit, mass unit, or acceleration unit is not recognized.

Usage Example:
    # Calculate the force from 10 pounds and 9.81 m/s², converting units to newton
    result = calculate_force(10, 9.81, force_unit='newton', mass_unit='pound', acceleration_unit='meter_per_second_squared')
    print(result)  # Output: 44.4822 N

    # Calculate the force from 10 pounds and 9.81 m/s², with the result including the unit
    result = calculate_force(10, 9.81, force_unit='kilonewton', mass_unit='pound', acceleration_unit='meter_per_second_squared', with_unit=True)
    print(result)  # Output: "0.0445 kN"

    # Calculate the force from 10 kilograms and 9.81 m/s², with the result including the unit
    result = calculate_force(10, 9.81, force_unit='pound_force', mass_unit='kilogram', acceleration_unit='meter_per_second_squared', with_unit=True)
    print(result)  # Output: "22.0462 lbf"
"""


from formulas.complex_formulas import force_calculator
from typing import Union
from operations import acceleration as ac
from operations import mass as m

fc = force_calculator.force_calculator

def calculate_force(mass: float, acceleration: float, force_unit: str = 'newton', mass_unit: str = 'kilogram', acceleration_unit: str = 'meter_per_second_squared', with_unit: bool = False) -> Union[float, str]:
    """
    Calculate the force based on mass and acceleration values, converting the units if necessary.

    This function calculates the force using the formula `Force = Mass * Acceleration`. It also handles unit conversions 
    for mass, acceleration, and force.

    Parameters:
    - mass (float): The mass value to be used in the force calculation.
    - acceleration (float): The acceleration value to be used in the force calculation.
    - force_unit (str): The unit in which the force should be returned. Default is 'newton'.
    - mass_unit (str): The unit of the provided mass. Default is 'kilogram'.
    - acceleration_unit (str): The unit of the provided acceleration. Default is 'meter_per_second_squared'.
    - with_unit (bool): Whether to include the unit in the result. Default is False, which returns only the numeric value.

    Returns:
    - Union[float, str]: The calculated force, either as a float (if `with_unit` is False) or a string 
      including the unit (if `with_unit` is True).

    Example:
    >>> calculate_force(10, 9.8)
    98.0
    >>> calculate_force(10, 9.8, force_unit='kilonewton', with_unit=True)
    '0.098 kilonewton'
    """

    # Convert mass to kilogram if necessary
    kilogram = m.mass_converter(mass, mass_unit, 'kilogram') if mass_unit != 'kilogram' else mass

    # Convert acceleration to meter_per_second_squared if necessary
    meter_per_second_squared = ac.acceleration_converter(acceleration, acceleration_unit, 'meter_per_second_squared') if acceleration_unit != 'meter_per_second_squared' else acceleration

    # Calculate force using the converted values
    return fc(kilogram, meter_per_second_squared, force_unit=force_unit, with_unit=with_unit)