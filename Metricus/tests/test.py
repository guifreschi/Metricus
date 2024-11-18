from operations.area import area_converter
from operations.electricity import electricity_converter
from operations.energy import energy_converter
from operations.length import length_converter
from operations.mass import mass_converter
from operations.pressure import pressure_converter
from operations.speed import speed_converter
from operations.temperature import temperature_converter
from operations.time import time_converter
from operations.volume import volume_converter
from operations.acceleration import acceleration_converter
from operations.force import force_converter
from operations.complex_operations import calculate_force
from operations.complex_operations import calculate_density
from operations.complex_operations import calculate_displacement
from operations.complex_operations import calculate_pressure

calculate_force = calculate_force.calculate_force
calculate_density = calculate_density.calculate_density
calculate_displacement = calculate_displacement.calculate_displacement
calculate_pressure = calculate_pressure.calculate_pressure

# help(area_converter)
# help(electricity_converter)
# help(energy_converter)
# help(length_converter)
# help(mass_converter)
# help(pressure_converter)
# help(speed_converter)
# help(temperature_converter)
# help(time_converter)
# help(volume_converter)
# help(acceleration_converter)
# help(force_converter)
# help(calculate_force)
# help(calculate_density)
# help(calculate_displacement)
# help(calculate_pressure)

print(area_converter(100, 'square_kilometer', 'hectare'))
print(electricity_converter(5, 'kilowatt', 'watt'))
print(energy_converter(10, 'calorie', 'joule'))
print(length_converter(5, 'kilometer', 'mile'))
print(mass_converter(1000, 'gram', 'pound'))
print(pressure_converter(1, 'atmosphere', 'pascal'))
print(speed_converter(100, 'kn', 'km/h'))
print(temperature_converter(25, 'celsius', 'fahrenheit'))
print(time_converter(1, 'hour', 'minute'))
print(volume_converter(1, 'm3', 'L'))
print(acceleration_converter(500, 'gal', 'gravity'))
print(force_converter(1000, 'newton', 'dyne'))
print(calculate_force(500, 10))
print(calculate_density(400, 500, mass_unit='tonne', volume_unit='L', with_unit=True))
print(calculate_displacement(100, 300, 'minute', with_unit=True))
print(calculate_pressure(500, 100, 'psi', 'poundal', with_unit=True))
