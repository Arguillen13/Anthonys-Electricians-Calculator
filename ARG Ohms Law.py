# Anthony's Electrician's Calculater / Ohm's Law

# Definitions for Ohm's Law variables:
# - e: Energy (Voltage), measured in volts
# - i: Current, measured in amps
# - r: Resistance, measured in ohms
# - p: Power, measured in watts

# Imports time module for delay of auto close
import time

# Welcome message
print("Welcome to Anthony's Ohm's Law Calculator")
time.sleep(1)

# Get User Input
while True:
    print("\nWhat do you want to calculate?")
    print("1. Voltage (e)")
    print("2. Current (i)")
    print("3. Resistance (r)")
    print("4. Power (p)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        known_variables = input("You want to calculate voltage! Enter the known variables (e.g., 'p i r'): ")
        if "i" in known_variables and "r" in known_variables:
            current = float(input("Enter the current in amps: "))
            resistance = float(input("Enter the resistance in ohms: "))
            voltage = resistance * current
            print(f"The voltage is {voltage} volts.")
            time.sleep(2)

        elif "i" in known_variables and "p" in known_variables:
            current = float(input("Enter the current in amps: "))
            power = float(input("Enter the power in watts: "))
            voltage = power / current
            print(f"The voltage is {voltage} volts.")
            time.sleep(2)

        elif "r" in known_variables and "p" in known_variables:
            resistance = float(input("Enter the resistance in ohms: "))
            power = float(input("Enter the power in watts: "))
            voltage = (power * resistance) ** 0.5
            print(f"The voltage is {voltage} volts.")
            time.sleep(2)

        else:
            print("Insufficient information to calculate voltage. Please provide at least two variables (e.g., 'p i r').")
            time.sleep(2)
            
    elif choice == "2":
        known_variables = input("You want to calculate current! Enter the known variables (e.g., 'p e r'): ")
        if "e" in known_variables and "r" in known_variables:
            energy = float(input("Enter the voltage in volts: "))
            resistance = float(input("Enter the resistance in ohms: "))
            current = energy / resistance
            print(f"The current is {current} amps.")
            time.sleep(2)

        elif "e" in known_variables and "p" in known_variables:
            energy = float(input("Enter the voltage in volts: "))
            power = float(input("Enter the power in watts: "))
            current = power / energy
            print(f"The current is {current} amps.")
            time.sleep(2)

        elif "p" in known_variables and "r" in known_variables:
            power = float(input("Enter the power in watts: "))
            resistance = float(input("Enter the resistance in ohms: "))
            current = energy / resistance
            print(f"The current is {current} amps.")
            time.sleep(2)

        else:
            print("Insufficient information to calculate current. Please provide at least two variables (e.g., 'p e r').")
            time.sleep(2)

    elif choice == "3":
        known_variables = input("You want to calculate resistance! Enter the known variables (e.g., 'p e i'): ")
        if "e" in known_variables and "i" in known_variables:
            energy = float(input("Enter the voltage in volts: "))
            current = float(input("Enter the current in amps: "))
            resistance = current / energy
            print(f"The resistance is {resistance} ohms.")
            time.sleep(2)

        elif "e" in known_variables and "p" in known_variables:
            energy = float(input("Enter the voltage in volts: "))
            power = float(input("Enter the power in watts: "))
            resistance = energy ** 2 / power
            print(f"The resistance is {resistance} ohms.")
            time.sleep(2)

        elif "i" in known_variables and "p" in known_variables:
            current = float(input("Enter the current in amps: "))
            power = float(input("Enter the power in watts: "))
            resistance = power / (current ** 2)
            print(f"The resistance is {resistance} ohms.")
            time.sleep(2)

        else:
            print("Insufficient information to calculate current. Please provide at least two variables (e.g., 'p e i').")
            time.sleep(2)

    elif choice == "4":
        known_variables = input("You want to calculate power! Enter the known variables (e.g., 'e i r'): ")
        if "i" in known_variables and "e" in known_variables:
            current = float(input("Enter the current in amps: "))
            energy = float(input("Enter the voltage in volts: "))
            power = current * energy
            print(f"The power is {power} watts.")
            time.sleep(2)

        elif "r" in known_variables and "i" in known_variables:
            resistance = float(input("Enter the resistance in ohms: "))
            current = float(input("Enter the current in amps: "))
            power = current ** 2 * resistance
            print(f"The power is {power} watts.")
            time.sleep(2)

        elif "e" in known_variables and "r" in known_variables:
            energy = float(input("Enter the voltage in volts: "))
            resistance = float(input("Enter the resistance in ohms: "))
            power = (energy ** 2) / resistance
            print(f"The power is {power} watts.")

        else:
            print("Insufficient information to calculate current. Please provide at least two variables (e.g., 'e i r').")
            time.sleep(2)

    elif choice == "5":
        print("Until next time! Goodbye!")

        #Add two second delay
        time.sleep(2)

        #Ends loop and program
        break