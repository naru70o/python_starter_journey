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
elif number %2 == 1:
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