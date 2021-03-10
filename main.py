import pygame 
from pygame import *
from pygame.constants import K_KP_ENTER
from src.start import Start as st
from src.ordination import Ordination as odt

colors = {"blue":(0, 0, 255), "white":(255, 255, 255), "green":(0, 255, 0), "black":(25,25,25)}
screen_size = (640, 420)
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('AlgoDataStuct')

# this is to control all the pages of thes aplication
link = {"start": st(), "ordination_algorithms": odt()}
current_layout = "start"

keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    if pygame.key.get_pressed()[K_KP_ENTER]:
        keep_going = not keep_going
    
    
    link[current_layout].animation(screen, colors)
    pygame.display.update()
