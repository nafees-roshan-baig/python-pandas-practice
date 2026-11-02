# x = int(input("Enter a number:"))
#
# if x > 0:
#     print("Positive")
# if x < 0:
#     print("Negative")
# if x == 0:
#     print(" 'zero' ")
# if x % 2 == 0:
#     print(' "even" ')
# if x%2 != 0:
#     print("Odd")

"""finding pass or fail """
# mark = float(input("Enter your mark:"))
#
# if mark >= 30:
#     print("Pass <3!")
# else:
#     print("Fail :(")

""" using esle """

# x = int(input("Enter a number:"))
#
# if x > 0:
#     print("Positive")
# else:
#     print("Negative")

"""using Elif"""
# marks = int(input("Enter your marks:"))
#
# if marks >85 and marks <=100:
#     print("A grade")
# elif marks >75 and marks <=85:
#     print("B grade")
# elif marks >65 and marks <=75:
#     print("C grade")
# elif marks >55 and marks <=65:
#     print("D grade")
# else:
#     print("fail !")
#
#
#
# x = str(input("enter the signal:"))
#
# if x == "green":
#     print("Gooo")
# elif x == "yellow":
#     print("ready to go")
# elif x == "red":
#     print("stop")
# else:
#     print("invalid")

"""using nested if"""
#
# age = int(input("Enter age:"))
#
# if age > 0:
#     if age >= 18:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Please enter an age above 0:")
#

username = input("Enter username:")
passw = input("Enter your password:")

if username == "admin" :
    if passw == "321":
        print("welcome")
    else:
        print("enter Valid password:")
else:
    print("not a valid username!")

