
# ask 5 marks from user calculate percentage and print it 


# 91-100  A
# 81-90 B

# 71-80 C
# 61-70 D
# 1-60 Fail
# Invalid 




sub1 = int(input("Enter the First subject :"))
sub2 = int(input("Enter the Second subject :"))
sub3 = int(input("Enter the Third subject :"))
sub4 = int(input("Enter the Fourth subject :"))
sub5 = int(input("Enter the Fifth subject :"))


marks_scored = sub1 + sub2 + sub3 + sub4 + sub5 


total_marks = 100 * 5

percentage = (marks_scored / total_marks) * 100
print(f"The marks scored by student is {marks_scored}")
print(f"The percentage scored by above student is {percentage}")

if percentage>= 91 and percentage<=100 :
    print("A grade")

elif percentage>= 81 and percentage<=90 :
    print("B grade")

elif percentage>= 71 and percentage<=80 :
    print("C grade")

elif percentage>= 61 and percentage<=70 :
    print("D grade")

elif percentage>= 1 and percentage<=60 :
    print("Failed")

else :
    print("Invalid result")

