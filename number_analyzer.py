# Number Analyzer

number = int(input("Enter a number: "))

# Positive, Negative or Zero
if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# Even or Odd
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Prime number check
if number < 2:
    print("The number is not Prime.")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is Prime.")
    else:
        print("The number is not Prime.")
