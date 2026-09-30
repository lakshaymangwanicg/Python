temp=float(input("Enter Temrature: "))
if temp<0:
    print("Freezing")
elif 0<temp<=15:
    print("Very Cold")
elif 16<=temp<=25:
    print("Cold")
elif 26<=temp<=35:
    print("Normal")
else:
    print("Hot")               