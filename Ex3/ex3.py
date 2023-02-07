from enum import Enum

class Color(Enum):
    black = 1
    white = 0
    green = 3
    red = 2
    
sorted_colors = sorted(list(Color), key=lambda c: c.value)
for color in sorted_colors:
    print("Sorted members name of Class Color: ", color.name)