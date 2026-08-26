numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
  division =  float(numerator) / float(denominator)
  print(f"{float(numerator)} \u00f7 {float(denominator)} = {division}")

except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")