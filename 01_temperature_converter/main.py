# Constants
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

# User input
celsius_input = 20
fahrenheit_input = 85

# Conversions
converted_to_f = (celsius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_c = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Display
print(f'{celsius_input}°C -> {converted_to_f:.1f}°F')
print(f'{fahrenheit_input}°F -> {converted_to_c:.1f}°C')

# HOMEWORK:
# Your homework is to create a miles-to-kilometers converter in Python!
#
# The script should:
# - Allow the user to convert from kilometers to miles and vice versa.
# - Display the formatted result in the console using f-strings.
#
# Remember, the homework is optional—but doing it will help you
# learn Python much faster than just watching me code.