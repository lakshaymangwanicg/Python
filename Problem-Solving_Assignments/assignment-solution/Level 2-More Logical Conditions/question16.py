unit=int(input("Enter your bill units: "))

extra_unit = unit-100
extra2_unit = unit-200

if unit<=100:
    print(f"your total bill is {unit*5}")

elif unit>100 and unit<=200:
    print(f"your total bill is {(100*5)+(extra_unit*7)}")
elif unit>200:
    print(f"Your total bill is {(100*5)+(100*7)+(extra2_unit*10)}")    
