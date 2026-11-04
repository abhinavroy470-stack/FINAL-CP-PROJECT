## MENU DRIVEN PROCESS
from data_analysis import Individual,Section,Compare
print("WELCOME TO THE DASHBOARD")
while True:
    choice1=input("Do you want to analyze personal(p)/class(c) statistics/compare(e) or exit(x) ? ")
    if(choice1=="p"):
        roll=input("Enter the roll number: ")
        a=Individual(roll)
        if not a.valid():
            print("Enter a valid roll number")
            break
        else:
            choice2=input("Do you want to know Subject-wise Marks(s)/ Grade(g)/ Bar-Graph(b): ")
            if(choice2=="s"):
                a.sub_marks()
            elif (choice2=="g"):
                a.grade()
            elif (choice2=="b"):
                a.bar()
            else:
                print("Enter a valid choice")
                break
    elif(choice1=="c"):
        b=Section()
        choice3=input("Do you want to know the class average(c)/ Subject-wise-average(s)/ Highest and Lowest marks(h)/ Full-Table(t): ")
        if(choice3=="c"):
            b.class_avg()
        elif (choice3=="s"):
            b.subject_avg()
        elif (choice3=="h"):
            b.highest_lowest()
        elif choice3=='t':
            b.table()
    elif(choice1=="e"):
        a1=input("Enter the first roll number: ")
        a2=input("Enter the second roll number: ")
        c=Compare(a1,a2)
        c.graph()
    elif(choice1=='x'):
        break




