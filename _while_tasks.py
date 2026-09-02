#1.Print Numbers
a=1
while a<11:
    print(a)
    a+=1

#2.Even Numbers
b=1
while b<=50:
    if b%2==0:
        print(b)
    b+=1
#3.Odd Numbers

c=1
while c<=50:
    if c%2!=0:
        print(c)
    c+=1

#4.Reverse Count
d=10
while d>0:
    print(d)
    d-=1

#5.Sum of Numbers
n=int(input("Enter a number:- "))
i=1
total=0
while i<=n:
    total+=i
    i+=1
print(total)

#6.Multiplication Numbers
num=int(input("Enter a number:- "))
i=1

while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1

#7.Count Numbers
end=int(input("Enter a number:- "))
start=2
count=0
while start<end:
    count+=1
    start+=1
print(count)


#8.Digit Count
e=int(input("Enter a number:- "))
digit_count=0
while e>0:
    digit_count+=1
    e=e//10
print(digit_count)

#9.Sum of Digits

f=int(input("Enter a number:- "))
sum=0
while f>0:
    r=f%10
    sum=sum+r
    f=f//10
print(sum)

#10.Reverse of a Number 
g=int(input("Enter a number:- "))
rev=0

while g>0:
    r=g%10
    rev=rev*10+r
    g=g//10
print(rev)

#11.Palindrome Number
f=int(input("Enter a number:- "))
rev=0
t=f
while f>0:
    r=f%10
    rev=rev*10+r
    f=f//10
if rev == t:
    print("Palindrome")
else:
    print("Not a palindrome")

#12.Count Even and Odd Digits
h=int(input("Enter a number:- "))
even_count=0
odd_count=0
while h>0:
    r=h%10
    if r%2==0:
        even_count+=1
    else:
        odd_count+=1
    h=h//10
print(even_count)
print(odd_count)

#13.Product of digits
i=int(input("Enter a number:-"))

product=1

while i>0:
    product=product*i%10
    i=i//10
print(product)


#14.Armstrong Numbers
j=int(input("Enter a number:-"))
sum=0
digit_count=0
f=j
while j>0:
    p=j%10
    digit_count+=1
    j=j//10
while j>0:
    p=j%10
    sum+=p**digit_count
    j=j//10
if sum==f:
    print("Armstrong")
else:
    print("Not an Armstrong")
    

#15.Prime Number
k=int(input("Enter a number:- "))
i=2
while i<k:
    if k%i==0:
        print("Not a Prime")
        break;
    else:
        print("Prime")
        break;

#16.Factors of a Number
m=int(input("Enter a number:- "))
i=1
while i<=m:
    if m%i==0:
        print(i)
    i+=1

#17.Perfect Number
p=int(input("Enter a number:- "))
i=1
n=0
while i<p:
    if p%i==0:
        n+=i
    i+=1
if p==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    
#18.HCF/GCD
r=int(input())
s=int(input())
i=1
temp=1
while i<=min(r,s):
    if r%i==0 and s%i==0:
        temp=i
    i+=1
print(temp)

#19.Decimal to Binary
t=int(input())
i=1
bi=0
while t>0:
    rem=t%2
    bi=bi+(rem*i)
    i*=10
    t=t//2
print(bi)
    

#20.Number Guessing Game
u=int(input("Enter a number:- "))
correct_guess=6
i=1

while i<=10:
    if u < correct_guess:
        print("Too Low")
        break;
    elif u > correct_guess:
        print("Too High")
        break;
    else:
        print("Correct Guess")
        break;





























