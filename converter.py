import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit.")
    parser.add_argument("temperature", type=float, help="The temperature value to convert")
    parser.add_argument("--to", choices=["C", "F"], required=True, help="Target temperature unit: C for Celsius, F for Fahrenheit")
    args = parser.parse_args()

    if args.to == "F":
        result = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C is {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F is {result:.2f}°C")

if __name__ == "__main__":
    main()
