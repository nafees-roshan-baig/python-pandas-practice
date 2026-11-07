# Basic Concepts:-
# Write a program to take 2 numbers and perform all arithmetic operations.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
# Check whether a number is even or odd.
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Find the largest of 3 numbers using conditional statements.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

"""------------------------------------------------------------------"""
# Loops
# Print numbers from 1 to 100 using a loop.
for i in range(1,100):
    print(i)
# Print the multiplication table of a given number
n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{i}x{n}={i*n}")
# Print all even numbers between 1–50.
for i in range(1,51):
    if i % 2 == 0:
        print(i)

"""----------------------------------------------------------"""
# Strings
# Reverse a string.
a = "Roshan"
for i in a[::-1]:
    print(i)
# Check whether a string is a palindrome.
a = input()
b = a[::-1]
if a == b :
    print("it is palindrome")
else:
    print("not a palindrome")
# Remove all spaces from a string.
a = input("Enter a string:")
a = a.replace(" ","")
print(a)
"""--------------------------------------"""
# Lists
# Create a list and find:
# Largest number
a = [20,30,10,40,60,50]
print(max(a))
# Smallest number
print(min(a))
# Remove duplicates from a list.
a=[1,1,2,2,3,3,3,4,4,4,5,5,5]
r=[]
for i in a:
    if not i in r:
        r.append(i)
print(r)
# Sort a list without using .sort().
numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# Count frequency of each element in a list.
numbers = [1, 2, 2, 3, 1, 2, 4]

for i in set(numbers):
    count = numbers.count(i)
    print(i, ":", count)
# Merge two lists and remove duplicates.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(a+b)

"""------------------------"""
# Tuples
# Create a tuple and:
t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("Length:", len(t))
print("First element:", t[0])
print("Last element:", t[-1])
# Find length
# Access elements
# Convert tuple to list and modify it.
t = (10, 20, 30)
lst = list(t)
lst[1] = 100
t = tuple(lst)
print(t)
# Count occurrences of an element in tuple.
t = (10, 20, 10, 30, 10, 40)
print("Occurrences:", t.count(10))
# Sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
# Perform:

# Union
# Intersection
# Difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
# Remove duplicates from a list using set.
numbers = [1, 2, 2, 3, 4, 4, 5]
result = list(set(numbers))
print(result)
# Check if one set is subset of another.
a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

"""-------------------------------"""
# Dictionaries
# Create a student dictionary (name, age, marks).
student = {
    "name": "Roshan",
    "age": 20,
    "marks": 85
}

print(student)
# Add and update values in dictionary.
student = {"name": "Roshan", "age": 20}

student["marks"] = 85
student["age"] = 21

print(student)
# Find the key with maximum value.
marks = {
    "Roshan": 85,
    "Harini": 92,
    "Pradeep": 78
}

largest = max(marks, key=marks.get)

print("Highest scorer:", largest)
print("Marks:", marks[largest])
# Merge two dictionaries.
a = {"name": "Roshan", "age": 20}
b = {"marks": 85, "city": "Chengalpattu"}

a.update(b)

print(a)
# Functions
# Function to calculate factorial.
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative integers")
else:
    print("Factorial:", factorial(n))
# Function with default arguments.
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Roshan")
# Function using keyword arguments.
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Roshan")
# Lambda Functions
# Use lambda to:

# Add two numbers
add = lambda a, b: a + b

print(add(10, 20))
# Find square of a number
square = lambda n: n * n

print(square(5))
# Modules
# Import math module and:
#
# Find square root
# Find factorial
import math

print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))

# Create your own module and import it.
import mymodule

print(mymodule.add(10, 20))
print(mymodule.square(5))
# Exception Handling
# Handle division by zero error.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")
# Handle invalid input using try-except.
try:
    n = int(input("Enter a number: "))
    print("Number:", n)

except ValueError:
    print("Please enter a valid integer")
# Use finally block example.
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Division error")

finally:
    print("Program completed")
# Create custom exception.
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Eligible")

except AgeError as e:
    print(e)
# File Handling
# Create a file and write student details.
file = open("student.txt", "w")

file.write("Name: Roshan\n")
file.write("Age: 20\n")
file.write("Marks: 85\n")

file.close()

print("Student details saved")
# Read contents from file.
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()
# Append data to existing file.
file = open("student.txt", "a")

file.write("City: Chengalpattu\n")

file.close()

print("Data appended successfully")