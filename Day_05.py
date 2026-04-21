
########################################
# String Operations

myName = "Rancho"
print(f"value = {myName}")
print(f"type  = {type(myName)}")

########################################
# Escape Sequences
# - `\t` : for long space
# - `\n` : for new line

print("I want to\tlearn Python\nIts a programming language.")

########################################
# len() function

myString = "Programming Language"
length = len(myString)
print(f"No of characters = {length}")

########################################
# 0-based indexing

myString = "Python"
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])
print(myString[5])

########################################
# Negative indexing

myString = "Python"
print(myString[-1])
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])
print(myString[-6])

########################################
# Changing case

myString = "RaNch0!?"
print(f"{myString.lower()}")
print(f"{myString.upper()}")

########################################
# Substring check

myString = "the cat sat on the mat"

print("cat" in myString)
print("at" in myString)
print("dog" in myString)
print()
print(myString.count("cat"))
print(myString.count("at"))
print(myString.count("dog"))
print()
print(myString.index("cat"))
print(myString.index("at"))
if("dog" in myString):
    print(myString.index("dog"))    # raises Error if "dog" isn't in myStr
else:
    print("dog not found")

########################################
# List & Dictionaries

myList = [5, 2, 1, 4]       # to store values
print(f"value = {myList}")
print(f"type  = {type(myList)}")
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1} # to store key:value pairs
print(f"value = {myDict}")
print(f"type  = {type(myDict)}")

########################################
# len() function

myList = [5, 2, 1, 4]
print(f"value = {myList}")
print(f"len   = {len(myList)}")
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}
print(f"value = {myDict}")
print(f"len   = {len(myDict)}")

########################################
# Indexing in lists

myList = [5, 2, 1, 4]
# 0-based indexing
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
# negative indexing
print(myList[-1])
print(myList[-2])
print(myList[-3])
print(myList[-4])

########################################
# Indexing in Dicts

# myList = [5, 6, 4]
myDict = {'Eng': 5, 'Sci': 6, 'Mat': 4}
# Key based indexing
print(myDict['Eng'])
print(myDict['Mat'])
print(myDict['Sci'])

########################################
# Membership check

myList = [5, 2, 1, 4]
print(5 in myList)  # slow
print(6 in myList)  # slow
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}
print('Eng' in myDict)      # fast
print(5 in myDict)      
print(5 in myDict.values()) # slow

########################################
# Adding new items

myList = [5, 2, 1, 4]

print(myList)
myList.append(7)
print(myList)
myList.insert(1, 8)
print(myList)

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}

print(myDict)
myDict['Sst'] = 4
print(myDict)

########################################
# Deleting existing items

myList = [8, 1, 4, 2, 0]

print(myList)
myList.pop(3)
print(myList)

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1, 'SSt': 4}

print(myDict)
myDict.pop('Mat')
print(myDict)

########################################
# For loop on string

myString = "Loop"
for ch in myString[1:3]:
    print(f"I am currently looking at {ch}")
print("Loop stopped!")

########################################
# For loop on list

myList = [8, 1, 4, 2, 0]
for num in myList:
    print(f"I am currently looking at {num}")
print("Loop stopped!")

########################################
# For loop on dictionary

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1, 'SSt': 4}
for key in myDict:
    print(f"I am currently looking at {myDict[key]}")
print("Loop stopped!")

########################################
# Running a loop for specified number of times

N = 4
for i in range(N):
    print(f"Hello {i}")
print("Loop stopped!")

########################################
# Nested Structures
# - We can store lists or dictionaries inside other lists or dictionaries
# - Structures liked these are called nested structures

########################################
# list of lists

nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested[0])}")
print()
print(nested)
print(nested[1])
print(nested[1][2])

########################################
# list of dicts

nested = [
    {'name':'Ronaldo', 'country':'Por', 'age':40},
    {'name':'Messi',   'country':'Arg', 'age':37},
    {'name':'Neymar',  'country':'Brz', 'age':30},
    {'name':'Ramos',   'country':'Spn', 'age':39},
]
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested[0])}")
print()
print(nested)
print(nested[1])
print(nested[1]['name'])

########################################
# dict of lists

nested = {
    'names' : ['Ronaldo', 'Messi', 'Neymar', 'Ramos'],
    'countries' : ['Por', 'Arg', 'Brz', 'Spn'],
    'ages' : [40, 37, 30, 39]
}
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested['names'])}")
print()
print(nested)
print(nested['names'])
print(nested['names'][2])

########################################
# dict of dicts

nested = {
    'left_forward' : {
        'name':'Ronaldo', 'country':'Portugal', 'age':40
    },
    'right_forward' : {
        'name':'Messi', 'country':'Argentina', 'age':37
    },
    'mid_fielder' : {
        'name':'Neymar', 'country':'Brazil', 'age':30
    },
    'center_back' : {
        'name':'Ramos', 'country':'Spain', 'age':39
    }
}
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested['left_forward'])}")
print()
print(nested)
print(nested['left_forward'])
print(nested['left_forward']['name'])

########################################
# Functions
# - A function is control block in programming language that performs a specific task
# - A function can have zero, one or more parameters (inputs)
# - A function can have zero, one or more return values (outputs)

########################################
# NO parameter, NO return value

def greet():
    print("Hello")

x = greet()
print(x)

########################################
# ONE parameter, NO return value

def greet(name):
    print(f"Hello {name}")

x = greet("Rancho")
print(x)

########################################
# NO parameter, ONE return value

def greet():
    print("Hello")
    return 7

x = greet()
print(x)

########################################
# ONE parameter, ONE return value
 
def greet(name):
    print(f"Hello {name}")
    return 7

x = greet("Rancho")
print(x)

########################################
# Function to find the greater of the two numbers

def max(a, b):
    if (a > b):
        return a
    else:
        return b
    
x = max(10, 20)
print(f"ans = {x}")

x = max(20, 10)
print(f"ans = {x}")

########################################