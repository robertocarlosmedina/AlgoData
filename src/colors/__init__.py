from enum import Enum

class color(Enum):
    blue=(0, 0, 255)
    white=(255, 255, 255)
    green=(0, 255, 0)
    black=(25,25,25)
    grey=(105, 105, 105)
    
# this is to return the RGB value of the color
def rgbColor(co):
    return [color_e.value for color_name, color_e in color.__members__.items() if co == color_name][0]
