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
"""