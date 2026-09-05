
#1
for i in range(1,11):
    print(i)

#2
for i in range(1,20):
    if i%2==0:
        print(i)

#3
n=int(input("Enter a number:- "))
total=0

for i in range(1,n+1):
    total+=i
print(total)


#4
m=int(input("Enter a number:- "))

for i in range(1,11):
    print(m,"*",i,"=",m*i)




#5
name="programming"
vow_count=0
for x in name:
    if x in "aeiou":
        vow_count+=1
print(vow_count)


#6
for i in range(1,11):
    print(i**2)


#7
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i)


#8
num=[4,8,15,16,23,42]
sum=0
for i in num:
    sum+=i
print(sum)
    


#9
num=[4,8,15,16,23,42]
largest=0
for i in num:
    if i>largest:
        largest=i
print(largest)

#10
str="hello"
rev_str=""
b=str[::-1]

for i in b:
    rev_str+=i
print(rev_str)
"""

"""
#While Loop
#1
i=10

while i>=1:
    print(i)
    i-=1

#2

i=1

while i<=10:
    print(i)
    i+=1


#3
inp=1
sum=0
while inp>0:
    inp=(int(input("Enter a number:- ")))
    sum+=inp
print(sum)



#4
i=1
correct_guess=7
while i<=10:
    i=int(input("Enter a number:- "))
    if i==7:
        print("Correct Guess")
        break
    else:
        print("Try Agian")
    


#5
num=12345
digit_count=0

while num>=1:
    num%10
    digit_count+=1
    num=num//10
print(digit_count)





#6

num=12345
rev=0
while num>=1:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)



#7
balance=1000
i=1
while balance>0:
    i=int(input("Enter an amount:- "))
    balance-=i
print(balance)
    



#8

i=1
while i<=30:
    if i%3==0:
        print(i)
    i+=1


#9
n=int(input("Enter a number:- "))
factorial=1
while n>0:
    factorial*=n
    n-=1
print(factorial)
    

#10


p_count=0

while p_count<3:
    
    password=input("Enter your password:- ")
    if password=="python123":
        print("Access Granted")
        break
    else:
        print("Invalid Password")
    p_count+=1
print("Timeout")

























