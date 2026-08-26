while True: 
    try:
        number = float(input("Enter a number: "))
        print(f"You entered: {number}")
        break

    except ValueError:
        print("That's not a valid number. Try again.")

