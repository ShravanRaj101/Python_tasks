"""List Tasks

1. Create a list containing 10 student names. Write a program to add a new student at the end, insert another
student at the beginning, and remove one student by name. Display the final list.
Ans:-"""

Student_names=["Shravan","manu","vicky","simha","simha","gokul","Jyo","Shravs","nikky","Baby"]

Student_names.append("siva")
print(Student_names)

Student_names.insert(0,"sindhu")
print(Student_names)

Student_names.remove("Shravs")
print(Student_names)

"""2. Given the list numbers = [12, 5, 8, 21, 5, 30, 8, 15], write a program to find the maximum value, minimum
value, total sum, and average of the numbers without using external libraries. 
Ans:-"""
nums=[12,5,8,21,5,30,8,15]

print("Max of nums: ",max(nums))
print("Min of nums: ",min(nums))
print("sum of nums: ",sum(nums))
print("Avg of nums: ",sum(nums)/len(nums))


"""3. Given numbers = [10, 20, 10, 30, 40, 20, 50], write a program to create a new list containing only unique
values while preserving their original order. 
Ans:-"""

numbers = [10, 20, 10, 30, 40, 20, 50]
r=list(dict.fromkeys(numbers))
print(r)

"""4. Given a list of numbers, write a program to separate the even numbers and odd numbers into two different
lists. Display both lists and their counts. 
Ans:-"""

nums_list=[1,2,3,4,5,6,7,8]
even_list=[] 
odd_list=[]
for i in nums_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list,"count of even list is:",len(even_list)) #output:-[2,4,6,8] count of even list is: 4
print(odd_list,"count of odd list is:",len(odd_list)) #output:-[1,3,5,7] count of odd list is: 4


"""5. Given marks = [78, 45, 92, 66, 35, 88, 55], write a program to sort the marks in ascending and descending
order, then display the top three marks."""
marks=[78,45,92,66,35,88,55]
marks.sort()
print(marks)   #output:-[35,45,55,66,78,88,92]
marks.sort(reverse=True)
print(marks)   #output:-[92,88,78,66,55,45,35]
print(marks[0:3])



"""Set Tasks

1. Create two sets: python_students and sql_students. """

python_students={"Shravan","Chinna","Manu","Vicky","Simha","Shravs"}
sql_students={"Jyo","Chinna","Nicky","Vicky"}

"""Find and display the students who are learning both
Python and SQL.
Ans:-"""
print(python_students.intersection(sql_students))

"""2. Using two sets of student names, find the students who are learning Python but not SQL. Also find the
students who are learning SQL but not Python.
 Ans:-"""
print(python_students-sql_students)
print(sql_students-python_students)

"""3. Create a set from a list containing duplicate values. Write a program to remove the duplicates and then
display the number of unique values.
 Ans:-"""

lis=[1,2,3,2,4,3,5,4]
s=set(lis)
print(s)
print(len(s))

"""4. Given two sets of numbers, demonstrate union, intersection, difference, and symmetric difference. Display 
the result of each operation with clear labels.
 Ans:-"""
s1={1,2,3,4,5,6,7,8}
s2={2,4,6,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))


"""5. Create a set of employee IDs. Write a program that accepts an employee ID from the user and checks 
whether that ID exists in the set. Display an appropriate message such as 'Employee ID found' or 'Employee ID 
not found'.
Ans:-"""

employee_id={101,102,103,104,105}
a=int(input("Enter your employee_id:- " ))
if a in employee_id:
    print("Employee ID found")
else:
    print("Employee ID not found")


"""Dictionary Tasks
1. Create a dictionary containing a student's name, age, course, and marks. Write a program to add a new key
    called city, update the marks, and display all key-value pairs. 
Ans:-"""
Student_Info={'name':'Shravan','age':24,'course':'MCA','marks':850}
print(Student_Info)
Student_Info.update({'city':'Warangal','marks':900})
print(Student_Info)
print(Student_Info.items())

"""2. Create a dictionary containing employee names as keys and their salaries as values. Write a program to find
    and display the employee with the highest salary and the employee with the lowest salary. 
Ans:-"""
Employee_in_hand={'Shravan':10000,'Manoj':15000,'Vicky':18000,'Simha':20000,'Chinna':25000}
print("Employee with highest salary is:",max(Employee_in_hand.values()))
print("Employee with lowest salary is:",min(Employee_in_hand.values()))

highest = max(Employee_in_hand.items(), key=lambda item: item[1])
lowest = min(Employee_in_hand.items(), key=lambda item: item[1])
print("Employee with highest salary is:",max(Employee_in_hand.values()))
print("Employee with lowest salary is:",min(Employee_in_hand.values()))


"""3. Given sales = {'Monday': 12000, 'Tuesday': 15000, 'Wednesday': 9000, 'Thursday': 18000, 'Friday': 14000},
    find the total sales, average sales, and day with the highest sales. 
Ans:-"""

sales= {'Monday': 12000, 'Tuesday': 15000, 'Wednesday': 9000, 'Thursday': 18000, 'Friday': 14000}

print(sum(sales.values()))
avg=sum(sales.values())/len(sales)
print(avg)
print(max(sales,key=sales.get))


"""4. Create a dictionary from two lists: names = ['Asha', 'Ravi', 'John'] and marks = [85, 72, 91]. The names
    should become keys and the marks should become values. Display the resulting dictionary. 
Ans:-"""
names=['Asha','Ravi','John']
marks=[85,72,91]
students=dict(zip(names,marks))
print(students)

"""5. Create a dictionary to store department-wise employee salaries. Example: {'IT': [45000, 55000, 60000], 'HR':
   [40000, 48000], 'Sales': [35000, 50000, 65000]}. Write a program to calculate the total salary and average
   salary for each department.
Ans:-"""

company={'IT': [45000, 55000, 60000], 'HR':
   [40000, 48000], 'Sales': [35000, 50000, 65000]}

for department,salaries in company.items():
    total_salaries=sum(salaries)
    average_salary=total_salaries/len(salaries)
print(total_salaries)
print(average_salary)

