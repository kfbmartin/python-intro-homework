number = int(input("Enter a number: "))

if number>0:
    print(f"{number} is positive.")

elif number< 0:
    print(f"{number} is negative.")

else:
    print(f"{number} is zero.")

if number !=0 and number%2 == 0:
    print(f"{number} is even.")

elif number !=0 and number%2 !=0:
    print(f"{number} is odd.")

else:
    print(f"{number} is even.")
