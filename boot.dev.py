# expected an indented block after function definition
# this error message appears when the function body is empthy
"""
def unlock_achievement(before_xp, ach_xp, ach_name):
"""

# identation error
# don't get fool idention always needs only 4 spaces
"""
def create_stats_message(strength, wisdom, dexterity):
      total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
    return msg
"""

    
############################# NUMBERS
################# 
'''
def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword+arrow+spear+dagger+fireball
    average_damage = total_damage / 5
    print(average_damage)
    return total_damage, average_damage

calculate_damage(2,4,2,45,6)
'''
################## Floor Division
'''
Python has great out-of-the-box support for mathematical operations. This, among other reasons, is why it has had such success in artificial intelligence, machine learning, and data science applications.

Floor division is like normal division except the result is floored afterward, which means the result is rounded down to the nearest integer. The // operator is used for floor division.

7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)

NOTE : it only down grade no matter what

floored = 17//3 # 5.66 :)
print(floored)
'''

##################### 
########### Exponents
'''
In both Python and mathematics, exponents represent repeated multiplication of a base number by itself a certain number of times.

double=2**2
print(double)
'''

####################
## Changing in Place
######## Plus Equals

'''
It's fairly common to want to change the value of a variable based on its current value.

# def update_player_score(current_score,increment):
def update_player_score(current_score):
    # current_score = current_score +increment
    current_score+=1
    print(current_score)
    return current_score

# update_player_score(20,1)
update_player_score(20)
'''

##################################
############## scientific notation
'''
scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally.


def max_players_on_server():
    small=1.024e18
    medium=1.0240e19
    large=1.024e20
    print(small,medium,large)

float=16
print(float)
max_players_on_server()
'''


#######################
## Bitwise “&” Operator
"""

bitways = 0b0101 & 0b0111
# bitways = 1 & 1
# print(bitways) 

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

user1_permissions = 0b1001  # Can create and edit
user2_permissions = 0b0100  # Can review only
user3_permissions = 0b0010  # Can delete only

print(f"User 1 can create: {get_create_bits(user1_permissions)}")   # Output: 0b1000 (True-ish)
print(f"User 1 can review: {get_review_bits(user1_permissions)}")   # Output: 0b0000 (False)
print(f"User 1 can delete: {get_delete_bits(user1_permissions)}")   # Output: 0b0000 (False)
print(f"User 1 can edit: {get_edit_bits(user1_permissions)}") # Output: 0b0001 (True-ish)

-------------------------------------------------

NOTE : Bitwise operators are special tools that allow you to directly manipulate these individual bits within a number.
and &
or |
"""

##############################
##############################
################# Damage Meter
"""
Assignment

Fix the intern's syntax error. The calculate_dps function should accept two arguments, but due to a syntax error, it's being called with 4 instead. Use the proper delimiter for thousands so that the numbers are still easy to parse visually.

The two numbers should be:

damage: 8 million, time: 45
damage: 10 million, time: 49

def main():
    calculate_dps(8, 45)
    calculate_dps(10, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
"""

##############################
##############################
################# Converting Binary


"""
The built-in int() function can convert a binary string to an integer. It takes a second argument that specifies the base of the number (binary is base 2). For example:

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4

-------------------------------------------------
# Assignment

def binary_string_to_int(num_servers, num_players, num_admins):
    data_a=int(num_servers,2)
    data_b=int(num_players,2)
    data_c=int(num_admins,2)
    return data_a,data_b,data_c

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6
"""


##################
###### for in Loop 

'''
def numbers():
    for i in range(0, 200,2): # start , end , increment
        print(i)

numbers()


# Assigment
Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of:

1 + 1 + 1 + 1 + 1...

we want:

0 + 1 + 2 + 3 + 4...

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
        print(i)

        
    return total

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end,2):
        total += i
        print(i, " : odd")

    return total

total = sum_of_numbers(0,4)
print(total)

total1 = sum_of_odd_numbers(12)
print(total1," total")
'''

"""
Assignment
In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers.

While regenerating health, a character first gains 1 health each iteration until it reaches the max_health amount.
The enemy_distance then shortens by 2 for each iteration.
If an enemy is at a distance of 3 or less from the character, the character is not able to regenerate health. (Flipping that, if an enemy is more than a distance of 3 from the character, then the character is able to regenerate health.)

def regenerate(current_health, max_health, enemy_distance):
    if ( enemy_distance <= 3):
        while current_health < max_health:
            current_health+=1
            
    return current_health

current_health = regenerate(0,100,1)        
print(current_health," current_health")

###### Match Countdown
###### We need a timer to countdown the start of PvP matches in Fantasy Quest.

def countdown_to_start():
    for i in range(10,-1,-1):
        print(f"{i}...")

countdown_to_start()        

def calculate_experience_points(level):
    total = level * 2
    return total    

level = calculate_experience_points(15);
print(level)
"""


##########################Reverse List
############################Assignment

"""
Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

reversed_items = []
def reverse_list(items):
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items

reverse_list(["c","b","a"])
print(reversed_items)

reversed_items = []
def reverse_list(items):
    for item in range(len(items),0,-1):
        reversed_item = items.pop()
        reversed_items.append(reversed_item)
        # print(item)
        print(reversed_item)

reverse_list([9,8,7,6,5,4,3,2,1])        
print(reversed_items)
"""

######################
######### Dictionaries

"""
Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.
"""
# def get_character_record(name, server, level, rank):
#     return {
#         "name": name,
#         "server": server,
#         "level": level,
#         "level": 1,
#         "rank": rank,
#         "rank": 2,
#         "id": f"{name}#{server}",
#     }

# object = get_character_record("kadar","2571sajd",29,9)
# print(object)

"""
A value is retrieved from a dictionary by specifying its corresponding key in square brackets. The square brackets look similar to indexing into a list.
"""

# car = {
#     "make": "Toyota",
#     "model": "Camry"
# }
# print(car["make"]) # you can't use indexing
# Prints: Toyota

"""
Updating Dictionary Values

If you try to set the value of a key that already exists, you'll end up just updating the value of that key.
"""

# planets = {
#     "Pluto": True,
# }
# planets["Pluto"] = False
# print(planets["Pluto"])
# Prints False

"""
Delition

You can delete existing keys using the del keyword.
"""

# planets = {
#     "Mercury": 0,
#     "Venus": 0,
#     "Earth": 1,
#     "Mars": 2,
#     "Jupiter": 79,
#     "Saturn": 9
# }

# del planets["Saturn"]
# print(planets)

"""
Checking for Existence

If you're unsure whether or not a key exists in a dictionary, use the in keyword.
"""

# cars = {
#     "ford": "f150",
#     "toyota": "camry"
# }

# print("ford" in cars)
# # Prints: True

# print("gmc" in cars)
# Prints: False


"""
Iterating Over a Dictionary in Python

We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list. With access to the dictionary's keys, we also have access to their corresponding values.
"""

# fruit_sizes = {
#     "apple": "small",
#     "banana": "large",
#     "grape": "tiny"
# }

# for name in fruit_sizes:
#     fruit_size=fruit_sizes[name]
#     print(f"name: {name}, size: {fruit_size}")


# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny