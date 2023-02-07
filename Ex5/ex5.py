from enum import Enum

class Color(Enum):
    black = 1
    white = 2
    green = 3
    red = 2
    
values = set(member.value for member in Color)
print(values)

# This program creates an enumeration class called Color with four members: RED, GREEN, BLUE, and YELLOW. 
# Then, it uses a set comprehension to extract the values of each member from the Color enumeration and 
# store them in a set called values. Since sets only store unique values, this will remove any duplicates in the values. 
# Finally, it prints the values set.