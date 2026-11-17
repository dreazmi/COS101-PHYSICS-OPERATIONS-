# COS 101 Assignment
# Physics Operations Using Functions and a While Loop

def calculate_density(mass, volume):
    return mass / volume

def calculate_pressure(force, area):
    return force / area

def calculate_momentum(mass, velocity):
    return mass * velocity

def calculate_power(work_done, time):
    return work_done / time

def calculate_potential_energy(mass, gravity, height):
    return mass * gravity * height


while True:
    print("\nPHYSICS OPERATIONS MENU")
    print("1. Density")
    print("2. Pressure")
    print("3. Momentum")
    print("4. Power")
    print("5. Gravitational Potential Energy")

    option = input("Select an operation (1-5): ")

    if option == "1":
        mass = float(input("Enter mass in kg: "))
        volume = float(input("Enter volume in m^3: "))
        if volume == 0:
            print("Volume must not be zero.")
        else:
            print("Density:", calculate_density(mass, volume), "kg/m^3")

    elif option == "2":
        force = float(input("Enter force in N: "))
        area = float(input("Enter area in m^2: "))
        if area == 0:
            print("Area must not be zero.")
        else:
            print("Pressure:", calculate_pressure(force, area), "Pa")

    elif option == "3":
        mass = float(input("Enter mass in kg: "))
        velocity = float(input("Enter velocity in m/s: "))
        print("Momentum:", calculate_momentum(mass, velocity), "kg m/s")

    elif option == "4":
        work_done = float(input("Enter work done in joules: "))
        time = float(input("Enter time in seconds: "))
        if time == 0:
            print("Time must not be zero.")
        else:
            print("Power:", calculate_power(work_done, time), "W")

    elif option == "5":
        mass = float(input("Enter mass in kg: "))
        gravity = float(input("Enter gravitational acceleration in m/s^2: "))
        height = float(input("Enter height in metres: "))
        print("Potential Energy:", calculate_potential_energy(mass, gravity, height), "J")

    else:
        print("Invalid option. Choose a number from 1 to 5.")

    response = input("\nWould you like to carry out another operation? (yes/no): ")
    if response.strip().lower() not in ("yes", "y"):
        print("Physics operations program ended.")
        break
