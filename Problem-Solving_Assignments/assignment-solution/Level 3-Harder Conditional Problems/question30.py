age=int(input("Enter your age: "))
marks=int(input("Enter your marks: "))
att=int(input("Enter your attendance percentage: "))
fam_inc=int(input("Enter family income: "))

if (18<=age<=25) and (marks>=85) and (att>=75) and (fam_inc<=300000):
    print("Scolarship Approved")
else:
    print("Scolarship Rejected\n Reason: Marks below 85")    
