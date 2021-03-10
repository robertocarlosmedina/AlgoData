from enum import Enum

class color(Enum):
    blue=(0, 0, 255)
    white=(255, 255, 255)
    green=(0, 255, 0)
    black=(25,25,25)
    
def addingColor(co):
    colr = color.green.name
    print(color.green.name)
    return colr