def celsius_to_fahrenheit(c):
    fahrenheit = round(((c * 9/5) + 32) , 1)
    #print(f"{c}\xb0C = {fahrenheit}\xb0F")
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = round(((f - 32) * 5/9), 1)
    return celsius
    #print(f"{f}\xb0F = {celsius}\xb0C")

print(f"0\xb0C = {celsius_to_fahrenheit(0)}\xb0F")
print(f"100\xb0C = {celsius_to_fahrenheit(100)}\xb0F")
print(f"72\xb0F = {fahrenheit_to_celsius(72)}\xb0C")