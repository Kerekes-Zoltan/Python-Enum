from enum import Enum

class Color(Enum):
    black = 1
    white = 3
    red = 2
    
values = [member.value for member in Color]
print("Values of members in Class Color: ", values)

# This program creates an enumeration class called Color with three members: RED, GREEN, and BLUE.
# Then, it uses a list comprehension to extract the values of each member from the Color enumeration and stores them 
# in a list called values. Finally, it prints the values list.