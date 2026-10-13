temp = float(input("Enter temperature: "))

while temp < -20 or temp > 45:
    print("Invalid temperature!")
    temp = float(input("Enter temperature again: "))

print("Accepted temperature:", temp)