#1 add two nums
def add(a,b):
    return a+b
print(add(10,20))

#2 substrct two nums
def sub(a,b):
    return a-b
print(sub(20,5))

#3 product of two nums
def mul(a,b):
    return a*b
print(mul(5,4))

#4 div of two nums
def div(a,b):
    return a/b
print(div(20,5))

#5 sqr of a num
def sqr(n):
    return n*n
print(sqr(5))

#6 cube of a num
def cub(n):
    return n*n*n
print(cub(3))

#7 double of a num
def doubl(n):
    return n*2#or n+n
print(doubl(100))

#8 half of a num
def haf(n):
    return n/2
print(haf(20))

#9 Even odd check
def check_even_odd(n):
    if n%2==0:
        return "Positive"
    else:
        return "Negative"
print(check_even_odd(9))

#10 positive or negative check
def check_num(n):
    if n>0:
        return "Positive"
    else:
        return "Negative"
print(check_num(9))

#11 positive,negative or zero check
def check_number(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"    
print(check_number(9))

#12 pass or fail
def result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
print(result(40))

#13 age check
def check_age(age):
    if age>=18:
        return "Major"
    elif age<0 or age>100:
        return "Invalid Age"
    else:
        return "Minor"
print(check_age(18))
#14 greatest of two nums
def greater(a,b):
    if a>b:
        return a
    else:
        return b
print(greater(10,25))

#15 samllest of two nums
def smaller(a,b):
    if a>b:
        return b
    else:
        return a
print(smaller(10,25))

#16 area of rectangle 

def rect_area(length,width):
    return length*width
print(rect_area(10,20))

#17 perimeter of rectangle
def rect_perimeter(length,width):
    return 2*(length*width)
print(rect_perimeter(10,20))

#18 Simple Interest
def simple_intrst(principal,rate,time):
    return (principal*rate*time)/100
print(simple_intrst(10000,10,2))

#19 total marls
def total_marks(m1,m2,m3):
    return m1+m2+m3
print(total_marks(70,85,90))

#20 Average marks
def avg_marks(m1,m2,m3):
    return (m1+m2+m3)/3
print(avg_marks(90,89,78))

#21 add with print result
def add(a,b):
    return a+b
result=add(10,20)
print(result)

#22 add with result product
def add(a,b):
    return a+b
result=add(10,20)*5
print(result)

#23 print(name)
def get_name(name):
    return name
print(get_name("Shravan"))

#24 print(result)
def pass_fail(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
result=pass_fail(70)
print(result)

#25 largest of three nums
def largest(a,b,c):
    if a>=b:
        if a>c:
            return a
        else:
            return c
    elif b>=c:
        if b>a:
            return b
    else:
        return c     
print(largest(50,50,10))



        
    



















