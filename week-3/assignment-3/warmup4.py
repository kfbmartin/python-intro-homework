number = int(input("Enter a number: "))

# if/elif/else statement 1 for sign

if number>0:
    print(f"{number} is positive.")

elif number< 0:
    print(f"{number} is negative.")

else:
    print(f"{number} is zero.")

# if/elif/else statement 2 for parity including zero

if number%2 == 0:
    print(f"{number} is even.")

elif number%2 !=0:
    print(f"{number} is odd.")

