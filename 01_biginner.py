import re

# conditionals
"""
# syntax

age=30
if age < 30:
    print("you are young")
elif age < 40:
    print("you are middle-aged")
else: print("age doesn't matter")
"""

######### exercise
# Easy: Write a program that checks if a number is even or odd.

"""
number=int(input())
if number % 2 == 0:
    print("this is even")
elif number % 2 == 1:
    print("this is odd")
else : print("this is unkonw")
"""

# Medium: Create a temperature classifier (e.g., "<0°C: Freezing", "0-20°C: Cool", ">20°C: Warm").

'''
tempreture=int(input())
if tempreture < 0:
    print(f"{tempreture} is so colllldddd")
elif tempreture > 0 and tempreture < 20 :
    print(f"{tempreture} is pretty normal")
elif tempreture > 20 :
    print(f"{tempreture} is so damb hotttttt")

'''

################# Loops
# For loop: Iterate through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# While loop: Countdown from 5
# count = 5
# while count < 0:
#     print(count)
#     count-=1

####### exercise
# Beginner: Write a loop to print all even numbers between 1 and 20.
"""
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
for even in numbers:
    if even % 2 == 0 :
        print(f"even numbers : {even}")

count=20
while count > 0:
    if count % 2 == 0:
        print(f"{count} this numbers are even")
    count=count-1

"""

# Advanced: Build a grading system that loops through a dictionary of student scores (e.g., {"Alice": 85, "Bob": 72}) and assigns letter grades (A/B/C/D/F)
# Sample student scores

'''
scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 58,
    "Frank": 80
}

# Function to assign letter grades
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Loop through the dictionary and assign grades
for student, score in scores.items():
    grade = assign_grade(score)
    print(f"{student}: {grade}")
print(scores)

######################Collections
############### sets,tuples,lists
#################################
#################################
#################################

# list are ordered and changeable. Allows duplicate members.
# tuple are ordered and unchangeable. Allows duplicate members.
# set are unordered and unindexed. No duplicate members.


############# Lists
###################
fruits=["apple","banana","cherry","apple"]
for fruit in fruits:
    print(f"this is different fruit {fruit}")

# help function is used to get information
print(help(fruits))

fruits=["apple","banana","cherry","apple"]

# fruits[0]="kiwi" # this will change the first item to kiwi

# fruits.append("kiwi") # this will add kiwi to the end of the list

# fruits.insert(1,"kiwi") # this will add kiwi to the second position

# fruits.remove("apple") # this will remove the first apple

# fruits.pop(1) # this will remove the second item

# fruits.clear() # this will clear the list

# fruits.sort() # this will sort the list

# fruits.reverse() # this will reverse the list

print(fruits)
'''

############ Sets
##################
# sets are unordered and unindexed. No duplicate members.but add and remove is faster than list

"""
fruits={"apple","banana","cherry","apple"}

# fruits.add("kiwi") # this will add kiwi to the set

# fruits.remove("apple") # this will remove the first apple

# fruits.discard("apple") # this will remove the first apple

# fruits.pop() # this will remove the first item

# fruits.clear() # this will clear the set

print(fruits)
"""

############ Tuples
# tuples are ordered and unindexed. No duplicate members. but add and remove is slower than list .

"""
fruits=("apple","banana","cherry","apple")

# fruits[1]="kiwi" # this will give an error because tuples are immutable

# fruits.append("kiwi") # this will give an error because tuples are immutable

# fruits.remove("apple") # this will give an error because tuples are immutable

# fruits.pop(1) # this will give an error because tuples are immutable

# fruits.clear() # this will give an error because tuples are immutable

print(fruits)
"""

################### Exercise
########## Weight coverter

"""
weight=float(input("Enter your weight: "))
unit=input("(L)bs or (K)g: ")
if unit.upper()=="L":
    print(f"You are {round(weight*0.453592,2)} kilos")
elif unit.upper()=="K":
    print(f"You are {round(weight/0.453592,2)} pounds")
else: 
    print("Invalid input")
"""

############### Strings
#######################

"""
# name="kadar"
# string methods
# print(name.upper()) # converts all the characters to uppercase
# print(name.lower()) # converts all the characters to lowercase and returns a new string
# print(name.isupper()) # checks if all the characters are uppercase
# print(name.islower()) # checks if all the characters are lowercase
# print(name.isalpha()) # checks if all the characters are alphabets and returns true if all the characters are alphabets
# print(name.isalnum()) # checks if all the characters are alphanumeric
# print(name.isnumeric()) # checks if all the characters are numeric
# print(name.startswith("k")) # checks if the string starts with the given character    
# print(name.endswith("r")) # checks if the string ends with the given character
# print(name.find("a")) # returns the index of the first occurrence of the given character
# print(name.replace("a","o")) # replaces all the occurrences of the given character with the new character
# print(name.split("a")) # splits the string at the given character and returns a list of strings
# print(name.match("k",name)) # checks if the string matches the given pattern

"""

##################
#### users handler

'''
users=[]
name=input("Enter your name: ")
email=input("Enter your email: ")

regex=r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
if not re.match(regex,email):
        print("Invalid email")
elif not name.lower().isalpha():
        print("Invalid name")
    
users.append({"name":name,"email":email})
print(users)
'''
