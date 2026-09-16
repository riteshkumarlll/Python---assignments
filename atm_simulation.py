# ATM Simulation

balance = 10000
pin = "1234"

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("\nLogin Successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Money deposited successfully.")
                print("New balance:", balance)
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", balance)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN.")
