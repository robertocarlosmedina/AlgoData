import pygame 
from pygame import *
from pygame.constants import K_KP_ENTER

screen_size = (640, 420)
colors = {"blue":(0, 0, 255), "white":(255, 255, 255), "green":(0, 255, 0), "black":(35,35,35)}
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('AlgoDataStuct')

## variables to the start display
global size = 40
global box_info = []
global y, x == 320, 210

def start(size):
    
    for i in range(4):
        box_info.append(1)
    box_pos = [((280, 170),"green"),((320, 170), "blue"), ((280, 210), "blue"),((320, 210), "green")]
    screen.fill(colors["black"])

    [pygame.draw.rect(screen, colors[info[1]], pygame.Rect(info[0][0], info[0][1], size, size)) for info in box_pos]

    if size>4:
        return size - 0.01
    else: 
        return 0

keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    if pygame.key.get_pressed()[K_KP_ENTER]:
        exit()


    size = start(size)
    
    pygame.display.update()