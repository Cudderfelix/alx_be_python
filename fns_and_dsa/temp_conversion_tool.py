# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 0.5556
CELSIUS_TO_FAHRENHEIT_FACTOR = 1.8

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt for temperature input and validate as numeric
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
        
        # Prompt for unit and validate
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return
        
        # Perform conversion based on unit
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {result:.1f}°F")
        else:  # unit == 'F'
            result = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {result:.1f}°C")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()