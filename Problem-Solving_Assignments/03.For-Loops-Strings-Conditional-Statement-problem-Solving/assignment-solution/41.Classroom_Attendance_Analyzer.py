p_count = 0
a_count = 0

for i in range(1,6): 
    print(f"Number {i} Attendance: ")
for j in range(1,3):
    print(f"Attendace of Number {j} day")
    pr = input("Enter Your Attendance:\nif you present then write 'p'\nif you are absent then write 'a'  ==>") 
    if pr=="p":
        p_count+=1
    if pr=="a":
        a_count+=1
print(p_count,a_count)
if p_count==5:
    