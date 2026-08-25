try:
    with open("../data/missing.txt", "r") as f:
        content = f.read()
    print("File read successfully.")

except FileNotFoundError as f:
    print(f"Error: {f} was not found. Please check the file path and try again.")

finally:
    print("Attempted file read.")   # runs in either case