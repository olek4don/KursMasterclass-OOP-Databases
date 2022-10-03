import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(0)
        except: # Should really be except ValueError:
            print("Invalid number entered, please try again.")
        finally:
            print("The finally clause always executes")

first_number = getint("Please enter the first number ")
second_number = getint("Please enter the second number ")

try:
    print(f"{first_number} divided by {second_number} is {first_number / second_number}")
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed sucessfully.")

############## My solution ###############

# def divide(a , b):
#     try:
#         return a/b
#     except (ZeroDivisionError, TypeError):
#         print("Don't do this.")


# a = divide(2, ) 

# print(a)
