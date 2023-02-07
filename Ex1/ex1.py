from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3
    
# get member name
print("Member Name: ", Color.red.name)

# get member value
print("Member Value: ", Color.red.value)