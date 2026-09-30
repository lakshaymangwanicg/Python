count = 0
for i in range(1,9):
    age = int(input("Enter Your age: "))
    distance = int(input("Enter Your Journey Distance: "))
    print(f"Your Entered age is: [{age}] and your Journey Distance is: [{distance} KM.]\nYour total fare is:")
    fare = distance*10
    if age<5:
        count+=0   
        print("Free")
    elif 5<=age<=12:
        fare1 = fare-fare*0.5
        count+=fare1
        print(fare1)
    elif age>60:
        fare2 = fare-fare*0.3
        count+=fare2
        print(fare2)
    else:
        fare3 = fare
        count+=fare3
        print(fare3)
print(f"The Total Amount of 8 Passenger is: [{count}]")
