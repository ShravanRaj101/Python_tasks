#1
numbers=[2,4,6,8]
c=map(lambda i:i+i,numbers)
print(list(c))


#2
numbers=[1,2,3,4,5]
x=map(lambda i:i**2,numbers)
print(list(x))

#3
numbers=[11,12,15,18,20,23,26]
x=filter(lambda i:i%2==0,numbers)
print(list(x))


#4
names=["Ram","Siva","Ramesh","Anusha","Raj"]
x=filter(lambda i:len(i)>4,names)
print(list(x))

#5
names=["Siva","Ravi","Kiran"]
ages=[22,24,21]
z=zip(names,ages)
print(list(z))

#6
a=[10,20,30,40]
b=[1,2,3,4]
x=(sum(x) for x in zip(a,b))
print(list(x))

#7
temperatures=[0,20,30,40]
a=map(lambda i:(i*9/5)+32,temperatures)
print(list(a))

#8
salary=[20000,30000,40000,50000]
b=map(lambda i:i+(i/10),salary)
print(set(b))

#9
marks=[25,35,67,30,89,45,20]
x=filter(lambda i:i>=35,marks)
print(list(x))

#10
prices=[500,1500,2500,800,3000]
x=filter(lambda i:i>1000,prices)
print(list(x))

#11
names=["Siva","Ravi","Anu","Kiran"]
department=["IT","HR","Finance","IT"]
d=zip(names ,department)
print(list(d))

#12
first_names=["Siva","Ravi","Anu"]
last_names=["Kumar","Teja"]

e=map(lambda x:x ,zip(first_names,last_names))
print(list(e))

#13
numbers=[10,25,55,60,75,40]
res=map(lambda x:x**2,filter(lambda i:i>50,numbers))
print(list(res))

#14
names=["Siva","ravi","anu","Kiran"]
salaries=[25000,45000,35000,20000]
res=filter(lambda i:i[1]>30000,zip(names,salaries))
print(list(res))

#15
names=["siva","ravi","anusha","kiran"]
res=map(lambda i:i.upper(),names)
print(list(res))




