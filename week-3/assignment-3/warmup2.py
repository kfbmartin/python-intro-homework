age = int(input("Enter your age:"))

if age>=0 and age<=12:
    print(f"Enter your age: {age}")
    print("You are a Child.")
elif age>=13 and age<=17:
    print(f"Enter your age: {age}")
    print("You are a Teen.")
elif age>=18 and age<=64:
    print(f"Enter your age: {age}")
    print("You are a Adult.")
else:
    print(f"Enter your age: {age}")
    print("You are a Senior.")
