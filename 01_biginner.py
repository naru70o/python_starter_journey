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
tempreture=int(input())
if tempreture < 0:
    print(f"{tempreture} is so colllldddd")
elif tempreture > 0 and tempreture < 20 :
    print(f"{tempreture} is pretty normal")
elif tempreture > 20 :
    print(f"{tempreture} is so damb hotttttt")
