# Example of using the Metricus package

# Necessary imports
from Metricus.gui import MetricusGUI
from Metricus import temperature_converter, time_converter
from Metricus import calculate_displacement
from Metricus.utilities import round_number


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

    # Initializing and running the graphical interface
    MetricusGUI()

# Executes the main function if the script is run directly
if __name__ == "__main__":
    main()
