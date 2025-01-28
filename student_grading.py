def student_grading_system(student_name,sub1,sub2,sub3,sub4,sub5):
    total=sub1+sub2+sub3+sub4+sub5     #calculate total marks
    percentage=(total/500)*100         #calculate total percentage
    if percentage>=85:
        grade='A'
    elif percentage>=65:
        grade='B'
    elif percentage>=35:
        grade='C'
    else:
        grade='Fail'
    return (f"Student Name: {student_name}\nTotal Marks: {total}\nPercentage: {percentage}\nGrade: {grade}")
def main():
    student_name=input("enter the name of student:")        #get input for name and marks.
    sub1 = int(input("Enter Marks for Subject 1:"))
    sub2 = int(input("Enter Marks for Subject 2:"))
    sub3 = int(input("Enter Marks for Subject 3:"))
    sub4 = int(input("Enter Marks for Subject 4:"))
    sub5 = int(input("Enter Marks for Subject 5:"))
    print(student_grading_system(student_name,sub1,sub2,sub3,sub4,sub5))
main()


