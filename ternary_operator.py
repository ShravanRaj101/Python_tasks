#1
a=int(input("Enter a number:- "))
result=("Positive" if a>=0
        else "Negative")
print(result)
#2
b=int(input("enter a number:- "))
even_odd=("Even" if b%2==0
          else "odd")
print(even_odd)
#3
age=int(input("Enter your age:- "))

vote=("Eligible to vote" if age>=18
      else "Not eligible")
print(vote)

#4
c=int(input("Enter a number:- "))
d=int(input("Enter a number:- "))

largest=("c is larger" if c>d
         else "D is larger")
print(largest)
#or
largest=(c if c>d
         else d)
print(largest)

#5
marks=int(input("Enter your marks:- "))
res=("Pass" if marks>35
     else "Fail")
print(res)

#2 Match Case
#1
day=int(input("Enter a number from 1 to 7:- "))

match(day):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
        
#2
e=int(input("Enter a number:- "))
f=int(input("Enter a number:- "))
operator=input("Enter a math symbol:- ")
match(operator):
    case "+":
        print(e+f)
    case "-":
        print(e-f)
    case "*":
        print(e*f)
    case "/":
        print(e/f)
    case _:
        print("Invalid Operator")

#3
Student_choice=int(input("Enter a number from 1 to 4:- "))
match(Student_choice):
    case 1:
        print("Add Student")
    case 2:
        print("View Student")
    case 3:
        print("Update Student")
    case 4:
        print("Delete Student")
    case _:
        print("Invalid Choice")

#4
grade=input("Enter a grade:- ")
match(grade):
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")
    
#5
traffic_color=input("choose from red,green,yellow:- ")
match(traffic_color):
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid Signal")
        


        
        
