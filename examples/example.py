# Example of using the Metricus package

# Necessary imports
from Metricus.gui import MetricusGUI
from Metricus import (
    temperature_converter,
    time_converter,
    acceleration_converter,
    calculate_displacement
)
from Metricus.utilities import (
    round_number,
    humanize_input,
    decomputarize_input,
    plot_temperature_variation
)


# Main function that demonstrates the converters and the graphical interface
def main():
    # ----------------------------
    # Temperature Conversion Example
    # ----------------------------
    temp_celsius = 25
    temp_rankine = temperature_converter(temp_celsius, 'celsius', 'rankine')
    print(f"{temp_celsius} degrees Celsius equals {temp_rankine} Rankine")

    # ----------------------------
    # Time Conversion Example
    # ----------------------------
    time_seconds = 3600
    time_hours = time_converter(time_seconds, 'second', 'hour')
    print(f"{time_seconds} seconds equals {time_hours} hours")

    # ----------------------------
    # Displacement Calculation Example
    # ----------------------------
    length_kilometers = 100
    speed_kmh = 100
    time_unit = 'minute'
    result = calculate_displacement(length=length_kilometers, speed=speed_kmh, time_unit=time_unit)
    print(f"Covering {length_kilometers} km at a speed of {speed_kmh} km/h takes {result} minutes.")

    # ----------------------------
    # Number Rounding Example
    # ----------------------------
    # Rounding a numeric result
    time_days = 365
    time_result = time_converter(time_days, 'day', 'year')
    rounded_number = round_number(time_result)
    print(f"The number {time_result} rounded is {rounded_number}")

    # Rounding a string result
    time_result_with_unit = time_converter(time_days, 'day', 'year', with_unit=True)
    rounded_number_with_unit = round_number(time_result_with_unit)
    print(f"The number {time_result_with_unit} rounded is {rounded_number_with_unit}")

    # ----------------------------
    # Humanizing and Decomputadorizing Input
    # ----------------------------
    from_acceleration = 'Meter per second squared'
    to_acceleration = 'Foot per second squared'

    # Humanizing input
    acceleration_result = acceleration_converter(
        100,
        humanize_input(from_acceleration),
        humanize_input(to_acceleration)
    )
    print(f"The conversion result from {from_acceleration} to {to_acceleration} is {acceleration_result}")

    # Decomputadorizing input
    decomputarized_from = decomputarize_input(humanize_input(from_acceleration))
    decomputarized_to = decomputarize_input(humanize_input(to_acceleration))
    print(f"The decomputarized input from '{humanize_input(from_acceleration)}' is '{decomputarized_from}'")
    print(f"The decomputarized input to '{humanize_input(to_acceleration)}' is '{decomputarized_to}'")

    # ----------------------------
    # Temperature Variation Plotting Examples
    # ----------------------------
    # Daily temperatures for 30 days (based on the provided list)
    temperatures = [
        15.3, 16.1, 14.8, 13.5, 12.4, 11.8, 13.0, 15.5, 16.2, 14.9,
        13.0, 12.5, 11.6, 13.4, 15.1, 11.0, 17.2, 18.5, 19.0, 18.3,
        17.8, 16.4, 15.0, 14.2, 13.6, 12.7, 13.8, 14.5, 15.2, 16.0
    ]

    # Example 1: Basic usage - Plot in Celsius with statistical info
    plot_temperature_variation(
        temperatures=temperatures,
        temperature_unit='celsius'
    )

    # Example 2: Convert temperatures to Fahrenheit
    plot_temperature_variation(
        temperatures=temperatures,
        temperature_unit='celsius',
        convert_to='fahrenheit'
    )

    # Example 3: Disable statistical information
    plot_temperature_variation(
        temperatures=temperatures,
        temperature_unit='celsius',
        convert_to='fahrenheit',
        with_info=False
    )

    # Example 4: Save the graph to a file
    plot_temperature_variation(
        temperatures=temperatures,
        temperature_unit='celsius',
        convert_to='fahrenheit',
        save_path='temperature_variation.png'
    )

    # Example 5: Save graph in Kelvin with statistics
    plot_temperature_variation(
        temperatures=temperatures,
        temperature_unit='celsius',
        convert_to='kelvin',
        save_path='temperature_variation_kelvin.pdf',
        with_info=True
    )

    # ----------------------------
    # Launching the Graphical Interface
    # ----------------------------
    MetricusGUI()

if __name__ == "__main__":
    main()
