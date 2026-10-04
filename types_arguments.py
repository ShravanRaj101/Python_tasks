#1

def greet(name):
    print("Hello",name)
greet("Ram")

#2

def add(a,b):
    print(a+b)
add(10,20)

#3

def student(name,age):
    print(name)
    print(age)
student(age=24,name="Shravan")

#4

def employee(name,salary=25000):
    print(name)
    print(salary)
employee("Rahul")
employee("Rahul",10000)

#5

def power(base,exponent=2):
    print(base**exponent)
power(3)
power(3,3)

#6

def area(length,width):
    print("Area is ",length*width)
area(6,4)
area(width=4,length=6)

#7

def login(username,password):
    print(username)
    print(password)
login(password=12345,username="cooldude69")

#8

'''
fun(10,20) is positional argument
fun(a=10,b=20) is keyword argument
fun(10,b=20) is default argument
'''

#9

def service(name,status="Active"):
    print(name)
    print(status)
service("recharge")
service("dth","Inactive")

#10

""""
def args(name):
    print(name)
args() #produces error due to missing argument
"""

#11

def bill(item,price,quantity=1,discount=0):
    print("Bill is",(item*quantity*price)/discount)
#bill(4,500)
bill(4,500,5,0.2)
bill(price=500,item=4,quantity=1,discount=15)

#12

def student_details(name,course='python',duration=3):
    print(name)
    print(course)
    print(duration)
student_details("shravan")
student_details("shravan",course="java")
student_details("shravan","full stack",6)

#13

def employee(name,dept,salary=30000,city="Hyderabad"):
    print(name,dept,salary,city)

employee("shravan","IT")
employee(dept="HR",name="ram",salary=35000,city="Kurnool")
employee("sudha",dept="security")

#14

def sal(basic,hra=0.20,da=0.10):
    print("salary is",basic+basic*hra+basic*da)
sal(10000)
sal(hra=0.4,da=0.2,basic=10000)
sal(20000,0.5,0.2)

#15

def connect(host,port=3306,user="root"):
    print(host,port,user)
connect("host1")
connect(user="admin",host="host 2",port=4567)
connect("host3",1234,"user1")
"""
Because in keyword arguments we specify variables in non uniform order
in positional arguments exact position order should be specified """

#16

def posi(a,b,c,d):
    print(a,b,c,d)
posi(10,20,30,40)
"""
posi(a=10,20,30,40)
"""

#17

def student(name="Siva",age=25):
    print(name,age)
student()

#18

def fun(a=10,b=20):
    print(a,b)
fun()

#19

def func(x,y=10,z=20):
    print(x,y,z)
func(10)
func(1,10,30)
func(x=2,y=345,z=3)

#20

def func(*,m1,m2,m3):
    print("Total Marks are:",m1+m2+m3)
    print("Average of Marks is:",m1+m2+m3/3)
func(m1=80,m2=70,m3=60)

#21

def total(*a):
    print(sum(a))
total(1,2,3,4,5,6,7,8,9)

#22

def ma(*b):
    print(max(b))
ma(1,2,3,4,5,6,7,8,9)

#23

def count_even(*c):
    count=0
    for i in c:
        if i%2==0:
            count+=1
    print("Even_Count is",count)

count_even(9,8,7,6,5,4,3,2,1)

#24

def avg(*d):
    if sum(d)==0:
        print("No arguments given")
    else:
        print(sum(d)/len(d))
avg()

#25

def student_marks(name,*marks):
    print(name)
    print("Subject Count is:",len(marks))
    print("Total Marks are:",sum(marks))
student_marks("Mia",40,50,60,70)

#26

def product(*e):
    product=1
    for i in e:
        product*=i
    print("Product is:",product)
product(1,2,3,4,5)

#27

def second_largest(*f):
    first_largest=0
    second_largest=0
    for  i in f:
        if i>first_largest:
            second_largest=first_largest
            first_largest=i
        elif i>second_largest and i!=first_largest:
            second_largest=i
    print(second_largest)
second_largest(9,4,9)

#28

def find_strings(*f):
    print(len(f))
find_strings("asdfghj","oiuyfdz","iuygfdx")

#29

def operation(operation,*numbers):
    if operation=="+":
        print(sum(numbers))
    elif operation=="*":
        print(max(numbers))
operation("+",9,8,7,6,5)
operation("*",9,8,7,6,5)

#30

"""
*args is used because it packs the number of
elements into a variable and returns them in a tuple
without that we would get error cause what if we
specify 4 args in function def and at the time of
function call we want to perform operation on less
than 4 or greater than 4 we would get error
"""

#31

def student(**kwargs):
    print(kwargs)
student(name="Shravan",roll_no=69,course="Python")

#32

def employee(**a):
    print(a)
employee(name="Mia",dept="It",salary=30000)

#33

def calculate_total(**b):
    print(b)
calculate_total(Maths=69,Science=70,social=80)

#34

def product(**details):
    print(details)
product(name="toy",type="plastic",price=250)

#35

"""
def filter_positive(**numbers):
    for i in numbers.items():
        if i>0:
            print(key[i])
filter_positive(x=100,y=-25,z=0,speed=45.5)
"""

#36

def check(**c):
    str_count=0
    int_count=0
    flot_count=0
    for i,j in c.items():
        if isinstance(j,str):
            str_count+=1
        elif isinstance(j,float):
            flot_count+=1
        elif isinstance(j,int):
            int_count+=1
    print(int_count)
    print(str_count)
    print(flot_count)        

check(a=10,b=20.0,c="kphb")

#37

def employee_report(**data):
    name = data.get('name', 'Unknown Employee')
    age = data.get('age', 'N/A')
    department = data.get('department', 'General')
    salary = data.get('salary', 0.0)
    
    print("Employee Report")
    print("Name",name)
    print("Age",age)
    print("Department",department)
    print("salary",salary)

employee_report(name="Alice", salary=75000)

#38

def emp(**d):
    print(max(d,key=d.get))
emp(ram=10000,bheem=20000,Koushik=30000)

#39

"""
diff b/t args and kwargs is that if we want to pass single values
we use args it returns the values in a tuple

coming to kwargs if we want to pass key value pairs we use kwargs
it returns the elements in a dictionary"""

#40

def both(*a,**b):
    print("these are args",a)
    print("these are kwargs",b)


both(1,2,3,4,5,name="Khalifa",age=33,profession="therapist")

#41

def fun(a,/,b,c=10):
    print(a)
    print(b)
    print(c)
"""a is positional only arg
b can be bot positional and keyword
c is default"""
fun(1,2)
fun(1,b=4)
fun(1,b=4,c=5)
fun(10,20,30)

#42

def employee(name,*,salary,department):
    print(name)
    print(salary)
    print(department)

"""name follows both positional and keyword arg
salary and dept follows keyword only arg"""

"valid calls"
employee("Sunny",salary=69000,department="Entertainment")
employee(name="Dani",salary=100000,department="Nurse")

"""invalid calls
employee("rachael",70000,"It")
employee(name="Lisa",80000,"police")
"""

#43

def calculate(a,b,/,operation="add",*,precision=2):
    if operation=="add":
        print(a+b)
    elif operation=="sub":
        print(a-b)
    elif operation=="mul":
        print(a*b)
    elif operation=="div":
        print(a/b)
    else:
        print("Value Error")
    print(precision)
"""
here a,b are strictly positional
operation can be both keyword and positional precision must be keyword only args"""
calculate(4,6,"sub",precision=3)
calculate(6,5,operation="mul",precision=4)

#44

def fun(a,b,/,c,d=10,*,e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
fun(1,2,4,e=3)
fun(1,2,c=3,d=5,e=8)
fun(1,2,c=3,e=9)

#45

"""
lets assume we are entering marks of a student it will be easier using
positional values of subjects as args
coming to keyword only args when entering details of a person it makes sense to
use keyword only args both have their positives
it allows us to explicitly enter the correct order and details
for every data
"""

#46

def report(name,*marks,grade="A"):
    print(name)
    print(*marks)
    print(grade)
b=90,80,87
report("Ava",69,67,89)
report("leah",b,grade="B")

#47

def dic(**kwargs):
    print(kwargs)
dic()
"It returns empty dictionary"

#48

def fun(a,/,c,d=10,*,e):
    print(a)
    print(c)
    print(d)
    print(e)
fun(1,4,e=3)
fun(1,c=3,d=5,e=8)
fun(1,c=3,e=9)

#49

def par(a,b=10,*c,**d):
    print(a)
    print(b)
    print(c)
    print(d)
par(10,20,1,2,3,4,name="Rajshri",roll=69)

#50

"""
positional only parameters (before /)
keyword only patrameters (after *)
variable length positional args(*args)
variable length keywords args(**args)
"""

#51

def calculate(op, *args, **kwargs):
    precision = kwargs.get('precision', 2)
    round_result = kwargs.get('roundresult', True)
    
    if not args:
        return 0
        
    if op in ('avg', 'average'):
        result = sum(args) / len(args)
        return round(result, precision) if round_result else result

    values = list(args)
    result = values[0]
    
    for num in values[1:]:
        if op in ('add', '+'):
            result += num
        elif op in ('sub', 'subtract', '-'):
            result -= num
        elif op in ('mul', 'multiply', '*'):
            result *= num
        elif op in ('div', 'divide', '/'):
            if num == 0:
                return "Error: Division by zero"
            result /= num
        else:
            return "Error: Unknown operator"
            
    return round(result, precision) if round_result else result

print(calculate('add', 5, 10, 15))

#52

def salary_report(name,basic,*allowances,tax=0,**deductions):
    print(name)
    salary=basic
    for i in allowances:
        a=basic/i
        salary=basic-a
        
    gross_salary=salary
    print("gross salary is",gross_salary)
    for i in deductions.values():
        b=gross_salary-i
    print("net salary i",b)
salary_report("divya",50000,10,20,tax=10,deduction=4000)

#53

def results(student_name,*marks,pass_marks=35,**subject_names):
    print(student_name)
    total=0
    avg=total/len(marks)
    for i in marks:
        if i>pass_marks and i<100:
            print("pass")
        elif i<pass_marks and i>0:
            print("fail")
        else:
            print("Invalid Marks")
    print("total marks",total)
    print("Average marks",avg)
    print(subject_names)

results("Alice", 45, 28, 95, 105, pass_marks=35, Math="Passed", Science="Failed")

#54

def order(name,*price,tax=10,discount=5):
    print(name)
    final_amount=0
    for i in price:
        final_amount+=i-i/10-i/5
    print(final_amount)
order("tanu",1000,2000,3000)

#55

"""
def results():
    pass
results()
results("Kevin", 90, 45, **["Math", "Pass"])
results("Julia", 85, **{"Math", "Science"})
results("Ian", *(77, 88), 99)
results(pass_marks=50, English="Pass")
results("Liam", 60, 70, pass_marks=40, pass_marks="High")
results("Hannah", [45, 90])
results("Noah", 55, student_name="Conflict")
results(student_name="George", 88, 92)
results("Fiona", 50, 60, student_name="Alex")
results("Evan", 75, 85, 35, History="Pass")
results("Diana", 80, 90, 40)
results(pass_marks=40, "Charlie", 90, 85)
results(Math="Fail", "Bob", 45, 75)
results(45, 80, student_name="Alice")
"""

#56

def employee(name,age,department,salary):
    return (name,age,department,salary)
print(*employee("mia",23,"it",100000))
data={"name":"mia","age":23,"department":"it","salary":100000}
print(*employee(**data))

#57
def par(a,b,c=10,*d,e,**f,):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

par(1, 2, e=5)
par(1, 2, 3, e=5)
par(1, 2, 3, 4, 5, 6, e=5)
par(1, 2, e=5, x=100, y=200)
par(1, 2, 3, 4, e=5, test="yes")
par(a=1, b=2, e=5)
par(1, b=2, c=30, e=5)
par(1, 2, 3, *[4, 5, 6], e=5)
par(1, 2, e=5, **{"status": 200, "user": "admin"})
par(1, 2, c=99, e=10, timeout=30)


#58
5,10

#59
5,10

#60
10,20

#61
10,20

#62
#error positional follows keyword

#63
(10,20,30)

#64
{a:10,b:20,c:30}

#65
{a:10,b:20}

#66
#1 find error
def test(**kwargs, *args):
    pass

#2 predict output
def sample(a, *args):
    print(a, args)
sample(1, 2, 3)

#3 predict output
def display(x, y):
    print(x + y)
display(**{'x': 10, 'y': 20})

#4 output
def demo(*args, mode):
    print(args, mode)
demo(1, 2, mode="fast")

#5 find error
def func(a, b):
    return a + b
func(**[1, 2])

#67
def profile(name, age, role):
    print("Name": name, "Age":age,"Role": role)
tup = ("Alice", 28, "Engineer")
profile(*tup)

dict = {"age": 28, "role": "Engineer", "name": "Alice"}
profile(**user_dict)


#68
def add(a,b):
    print(a+b)
add(10,20)

def student(name,age):
    print(name)
    print(age)
student(age=24,name="Shravan")

def employee(name,salary=25000):
    print(name)
    print(salary)
employee("Rahul")
employee("Rahul",10000)

def power(base,exponent=2):
    print(base**exponent)
power(3)
power(3,3)

def area(length,width):
    print("Area is ",length*width)
area(6,4)
area(width=4,length=6)






