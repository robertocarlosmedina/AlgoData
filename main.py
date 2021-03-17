import pygame 
from pygame.locals import *
from src.colors import color
from src.menu import Menu
from src.start import Start as st
from src.ordination import Ordination as odt

screen_size = (640, 420)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('AlgoDataStuct')

# this is to control all the pages of thes aplication
links = {"start": st(), "menu": Menu(), "ordination_algorithms": odt()}
current_layout = "ordination_algorithms"
# current_layout = "start"

theme = True
keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_KP_ENTER]:
                exit()
                
            elif pygame.key.get_pressed()[K_t]:
                theme = not theme
    
    # Working on theme change later
    screen.fill(color.black.value) if theme else screen.fill(color.white1.value)

    current_layout = links[current_layout].run(screen, screen_size)
    pygame.display.update()
