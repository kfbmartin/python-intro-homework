age = int(input("Enter your age:"))

if age>=0 and age<=12:
    #print(f"Your age is {age}.")
    print("Child.")
elif age>=13 and age<=17:
    #print(f"Your age is {age}.")
    print("Teen.")
elif age>=18 and age<=64:
    #print(f"Your age is {age}.")
    print("Adult.")
else:
    #print(f"Your age is {age}.")
    print("Senior.")
