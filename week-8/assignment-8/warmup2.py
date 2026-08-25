numerator = int(input("Enter the numerator:"))
denominator = int(input("Enter the denominator:"))

try:
  division =  numerator / denominator
  print(f"{numerator} \u00f7 {denominator} = {division}")

except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")