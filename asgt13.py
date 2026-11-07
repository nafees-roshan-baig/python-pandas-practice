# 1. Division by Zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# 2. Invalid Integer Input
try:
    n = int(input("Enter a number: "))
    print(n)
except ValueError:
    print("Invalid input")


# 3. String to Integer Conversion
try:
    n = int("abc")
    print(n)
except ValueError:
    print("Invalid conversion")


# 4. List Index Error
a = [10, 20, 30, 40, 50]
try:
    i = int(input("Enter index: "))
    print(a[i])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Enter a valid integer")


# 5. Dictionary Key Error
a = {"name": "Roshan", "age": 20, "city": "Chennai"}
try:
    key = input("Enter key: ")
    print(a[key])
except KeyError:
    print("Key does not exist")


# 6. File Not Found
try:
    f = open("student.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")


# 7. Type Error
try:
    a = 10
    b = "hello"
    print(a + b)
except TypeError:
    print("Cannot add int and string")


# 8. Negative Age Validation
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError
    print("Age:", age)
except ValueError:
    print("Invalid age")


# 9. Try-Except-Else
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)


# 10. Continuous Input Until Valid
while True:
    try:
        n = int(input("Enter a number: "))
        print("Valid number:", n)
        break
    except ValueError:
        print("Invalid input! Try again.")