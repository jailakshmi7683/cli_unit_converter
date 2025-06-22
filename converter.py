import argparse

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Main function
def main():
    # Create a parser for command-line arguments
    parser = argparse.ArgumentParser(
        description="Convert temperature between Celsius and Fahrenheit"
    )

    # Add argument for temperature value (required)
    parser.add_argument(
        "temperature",
        type=float,
        help="Temperature value to convert"
    )

    # Add required flag to choose the target unit
    parser.add_argument(
        "--to",
        choices=["C", "F"],
        required=True,
        help="Target unit: C for Celsius, F for Fahrenheit"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Do the conversion based on --to option
    if args.to == "F":
        result = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C is {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F is {result:.2f}°C")

if __name__ == "__main__":
    main()
