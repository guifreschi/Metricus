# Example of using the Metricus package

# Necessary imports
from Metricus.gui import MetricusGUI
from Metricus import temperature_converter, time_converter, acceleration_converter
from Metricus import calculate_displacement
from Metricus.utilities import round_number, humanize_input, decomputarize_input


# Main function that demonstrates the converters and the graphical interface
def main():
    # Converting temperatures
    temp_celsius = 25
    temp_rankine = temperature_converter(temp_celsius, 'celsius', 'rankine')
    print(f"{temp_celsius} degrees Celsius equals {temp_rankine} Rankine")

    # Converting time
    time_seconds = 3600
    time_hours = time_converter(time_seconds, 'second', 'hour')
    print(f"{time_seconds} seconds equals {time_hours} hours")

    # Calculating displacement
    length_kilometers = 100
    speed_kmh = 100
    time_unit = 'minute'
    result = calculate_displacement(length=length_kilometers, speed=speed_kmh, time_unit=time_unit)
    print(f"Covering {length_kilometers} km at a speed of {speed_kmh} km/h takes {result} minutes.")

    # Rounding a result
    time_days = 365
    time_result = time_converter(time_days, 'day', 'year')
    rounded_number = round_number(time_result)
    print(f"The number {time_result} rounded is {rounded_number}")

    # Rounding a str result 
    time_result = time_converter(time_days, 'day', 'year', with_unit=True)
    rounded_number = round_number(time_result)
    print(f"The number {time_result} rounded is {rounded_number}")

    # Humanizing input
    from_acceleration = 'Meter per second squared'
    to_acceleration = 'Foot per second squared'
    acceleration_result = acceleration_converter(100, humanize_input(from_acceleration), humanize_input(to_acceleration))
    print(f"The conversion result from {from_acceleration} to {to_acceleration} is {acceleration_result}")

    # Decomputadorize input
    decomputarized_from = decomputarize_input(humanize_input(from_acceleration))
    decomputarized_to = decomputarize_input(humanize_input(to_acceleration))
    print(f"The decomputarized input from '{humanize_input(from_acceleration)}' is '{decomputarized_from}'")
    print(f"The decomputarized input to '{humanize_input(to_acceleration)}' is '{decomputarized_to}'")

    # Initializing and running the graphical interface
    MetricusGUI()

# Executes the main function if the script is run directly
if __name__ == "__main__":
    main()
