# Car Drive Simulation

speed = 0

while True:
    print("\n--- CAR DRIVE SIMULATION ---")
    print("1. Start Car")
    print("2. Accelerate")
    print("3. Brake")
    print("4. Show Speed")
    print("5. Stop Car")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Car started.")

    elif choice == "2":
        speed += 10

        if speed > 120:
            speed = 120
            print("Maximum speed reached!")
        else:
            print("Car accelerated.")
            print("Current speed:", speed, "km/h")

    elif choice == "3":
        speed -= 10

        if speed < 0:
            speed = 0

        print("Car slowed down.")
        print("Current speed:", speed, "km/h")

    elif choice == "4":
        print("Current speed:", speed, "km/h")

    elif choice == "5":
        speed = 0
        print("Car stopped.")

    elif choice == "6":
        print("Exiting simulation...")
        break

    else:
        print("Invalid choice.")
