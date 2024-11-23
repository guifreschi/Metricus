"""
Project: Metricus - Unit Converters

Description:
Metricus is a project designed to perform accurate conversions between various measurement units. 
It features an intuitive graphical user interface (GUI) built with the `tkinter` module and supports both simple conversions and complex calculations. 
Additionally, the project will be made available on PyPI for easy installation and use by developers and end-users.

Key Features:
--------------
1. Graphical User Interface:
    - User-friendly and responsive interface developed using `tkinter`.
    - Easy navigation to select converters and perform calculations.

2. Simple Converters:
    - **Acceleration**: Converts between units like m/s², ft/s², g, and more.
    - **Area**: Converts between square meters, hectares, acres, and others.
    - **Energy**: Converts between joules, calories, kWh, and others.
    - **Electricity**: Converts between amperes, volts, ohms, and others.
    - **Force**: Supports Newton, Dyne, Pound-force, and other units.
    - **Length**: Converts between meters, miles, inches, feet, and more.
    - **Mass**: Converts between kilograms, grams, tons, and more.
    - **Pressure**: Supports Pascal, Bar, PSI, and other pressure units.
    - **Speed**: Converts between km/h, m/s, mi/h, and other units.
    - **Temperature**: Converts between Celsius, Fahrenheit, Kelvin, and more.
    - **Time**: Converts between seconds, minutes, hours, days, and more.
    - **Volume**: Converts between liters, gallons, milliliters, and other units.

3. Complex Converters:
    - **calculate_density**: Calculates density based on provided mass and volume.
    - **calculate_displacement**: Calculates displacement using the formula \( s = v \times t \) (speed × time).
    - **calculate_force**: Calculates force using the formula \( F = m \times a \) (mass × acceleration).
    - **calculate_pressure**: Calculates pressure using the formula \( P = F / A \) (force ÷ area).

Project Structure:
-------------------
- **interface/**: Contains modules related to the graphical user interface.
    - `main_window.py`: Main configuration of the graphical interface.
    - `input_fields.py`: Creation and organization of input fields.
    - `result_display.py`: Display of results.
- **operations/**: Modules responsible for calculations and conversions.
    - `basic_converters.py`: Implementation of simple converters.
    - `complex_calculators.py`: Implementation of complex calculation functions.
- **utils/**: Utility modules to support the project.
    - `exceptions.py`: Definitions of custom exceptions.
    - `formatters.py`: Functions to format results and messages.
- **tests/**: Automated tests to ensure the functionality and accuracy of the project.

Requirements:
--------------
- Python 3.8 or higher.
- External dependencies:
    - `tkinter`: Included in the Python standard library for graphical interfaces.

Installation:
--------------
Metricus will be available on PyPI. To install, use the following command:

```sh
pip install Metricus
"""