########################################
# Basic IO operations

print("Hello")

########################################
# print() function

print("123")    # gives 123
print(123)      # gives 123
print()         # gives an empty line
print("abc")    # gives abc
print(abc)      # raises Error

########################################
# Variables

xyz = 456       # here xyz is a variable

print("xyz")    # gives xyz, prints it as it is
print(xyz)      # gives 456, prints the value of xyz

########################################
# input() function

xyz = input()   # here xyz is a variable

print("xyz")
print(xyz)

########################################

name = "Rancho"
# print multiple values in multiple lines
print("Hello")
print(name)
print("How are you?")
print()
# print multiple values in the same line by separating them using commas
print("Hello",name," How are you?")
print()
# print multiple values in the same line by using f-strings
print(f"Hello {name} How are you?")

########################################
# type() function

var = 12
print(type(12))
print(type(var))
print()

var = 3.4
print(type(3.4))
print(type(var))
print()

var = "56"
print(type("56"))
print(type(var))
print()

var = True
print(type(var))
print(type(True))

########################################

name = input("Enter your name: ")
print(f"value = {name}, type = {type(name)}")

number = input("Enter a number: ")
print(f"value = {number}, type = {type(number)}")

########################################
# Type casting

a = input("Enter a number: ")
print(f"value = {a}, type = {type(a)}")

a = int(a)
print(f"value = {a}, type = {type(a)}")

########################################

a = input("Enter a number: ")
b = input("Enter another number: ")

print(f"Before typecasting: {a} + {b} = {a + b}")

a = int(a)
b = int(b)

print(f"After typecasting : {a} + {b} = {a + b}")

########################################
# Arithmetic operators
# - Inputs are numbers
# - Output is number
# [`+`, `-`, `*`, `/`]

a = 22
b = 7

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

########################################
# Relational operators
# - Inputs are numbers
# - Output is boolean
# [`==`, `!=`, `<`, `>`, `<=`, `>=`]

a = 2
b = 7

print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}")
print(f"{a} <  {b} = {a < b}")
print(f"{a} >  {b} = {a > b}")

########################################
# Logical operators
# - Inputs are boolean
# - Output is boolean
# [`not`, `and`, `or`]

a = True
b = False

print(f"not {a} = {not a}")
print(f"not {b} = {not b}")
print()
print(f"{a} or  {b} = {a or b}")
print(f"{a} and {b} = {a and b}")

########################################
# Conditions
# - Expressions that result in a boolean value (i.e. either True or False).
# - These are used to alter the flow of the program at runtime.

a = 4
b = 5

a_is_positive = a > 0
b_is_positive = b > 0
both_positive = a_is_positive and b_is_positive

print(f"Is a positive?      {a_is_positive}")
print(f"Is b positive?      {b_is_positive}")
print(f"Are both positive?  {both_positive}")

########################################
# Conditional statements
# These statements allow us to take decisions at runtime,
# based on some condition.

########################################
# if statement

condition = False

print(1)

if (condition):
    print(2)
    print(3)

print(4)

########################################
# else statement

condition = False

print(1)

if (condition):
    print(2)
else:
    print(3)

print(4)

########################################
# if-elif-else statement

condition1 = True
condition2 = True
condition3 = True

print(1)

if (condition1):
    print(2)

elif(condition2):
    print(3)

elif(condition3):
    print(4)

else:
    print(5)

print(6)

########################################
# while loop

count = 0

print(f"Before : {count}")

while (count < 5):
    print(f"Inside : {count}")
    count = count + 1

print(f"After  : {count}")

########################################
# We have to search for an unknown number
# selected by a person in a given range (say 1 to 100).
# After each guess, the other person will reply with either or these:
# - my number is higher than your guess
# - my number is lower than your guess
# - my number is equal to your guess
# Based on the response, you have to make a new guess.
# The game continues until you find the correct number.

########################################
# **Approach 1** (Linear Search)
# Check for each number in the given range,
# starting from the lowest to the highest,
# until you find the correct number.
# As you can see, this is going to be very slow.

lower_bound = 1
upper_bound = 100

print(f"Think of a number between {lower_bound} and {upper_bound}")

guess = lower_bound
match_found = False

while(guess <= upper_bound and not match_found):
    print(f"My guess is {guess}")
    response = input("Select response (< = >): ")
    guess = guess + 1

    if(response == "="):
        print("I won!")
        match_found = True
        break

########################################
# **Approach 2** (Binary Search)
# Instead of checking of all numbers from start till end,
# we check for the middle number. This will result in 3 cases:
# - it matches with the unknown number:
#       we win
# - its lower the unknown number:
#       in this case will eliminate the lower half of the range
# - its higher the unknown number:
#       in this case will eliminate the upper half of the range
# So just a simple guess will reduce the range by half.

lower_bound = 1
upper_bound = 100

print(f"Think of a number between {lower_bound} and {upper_bound}")

match_found = False

while(lower_bound <= upper_bound and not match_found):
    guess = (lower_bound + upper_bound) // 2

    print(f"My guess is {guess}")
    response = input("Select response (< = >): ")
    if(response == "<"):
        upper_bound = guess - 1
    elif(response == ">"):
        lower_bound = guess + 1
    elif(response == "="):
        print("I won!")
        match_found = True
        
########################################