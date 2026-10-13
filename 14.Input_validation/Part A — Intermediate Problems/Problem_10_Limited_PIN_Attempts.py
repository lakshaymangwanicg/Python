pin = 2468
attempts = 0

while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))
    attempts = attempts + 1

    if entered_pin == pin:
        print("Access granted")
        break
    else:
        print("Wrong PIN")

if attempts == 3 and entered_pin != pin:
    print("Access denied")