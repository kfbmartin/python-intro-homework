numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:

  numerator = float(numerator)
  denominator = float(denominator)

  division =  numerator / denominator

  print(f"{numerator} \u00f7 {denominator} = {division}")

except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")