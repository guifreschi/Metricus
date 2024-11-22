# Example of using the Metricus package

# Necessary imports
from Metricus.gui import MetricusGUI
from Metricus.operations import temperature_converter, time_converter

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

    # Initializing and running the graphical interface
    MetricusGUI()

# Executes the main function if the script is run directly
if __name__ == "__main__":
    main()
