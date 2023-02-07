from enum import Enum

class Color(Enum):
    black = 0
    white = 1
    red = 2
    green = 3
    
for member in Color:
    print(f"{member.name} : {member.value}")