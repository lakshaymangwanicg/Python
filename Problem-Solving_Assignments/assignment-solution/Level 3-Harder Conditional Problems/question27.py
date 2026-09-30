hours=int(input("Enter hours: "))
minute=int(input("Enter minute: "))
second=int(input("Enter second: "))
if 0<=hours<=23 and 0<=minute<=59 and 0<=second<=59:
    print("Valid Time")
else:
    print("Invalid Time")    