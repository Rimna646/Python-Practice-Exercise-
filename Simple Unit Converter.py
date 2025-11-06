# Simple Unit Converter

# Define the conversion function
def convert_unit(value, conversion_type):
    if conversion_type == 'C2F':
        # Celsius to Fahrenheit
        result = (value * 9/5) + 32
        return f"{value}°C is {result}°F"
    elif conversion_type == 'F2C':
        # Fahrenheit to Celsius
        result = (value - 32) * 5/9
        return f"{value}°F is {result}°C"
    elif conversion_type == 'M2F':
        # Meters to Feet
        result = value * 3.28084
        return f"{value} meters is {result} feet"
    elif conversion_type == 'F2M':
        # Feet to Meters
        result = value / 3.28084
        return f"{value} feet is {result} meters"
    else:
        return "Invalid conversion type. Please use C2F, F2C, M2F, or F2M."

# Ask the user for input
value = float(input("Enter the value to convert: "))
conversion_type = input("Enter conversion type (C2F, F2C, M2F, F2M): ")

# Perform conversion and display the result
print(convert_unit(value, conversion_type))
