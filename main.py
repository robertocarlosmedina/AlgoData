import pygame 
from pygame.locals import *
from src.colors import color
from src.start import Start
from src.ordination import Ordination

screen_size = (640, 420)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('AlgoDataStruct')

# this is to control all the pages of thes aplication
links = {"start": Start(), "ordination_algorithms": Ordination()}
current_layout = "ordination_algorithms"
# current_layout = "start"

theme = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    if pygame.key.get_pressed()[K_KP_ENTER]:
        exit()
    elif pygame.key.get_pressed()[K_t]:
        pygame.time.delay(100)
        theme = not theme
    
    # I'll Work on theme change later
    screen.fill(color.black.value) if theme else screen.fill(color.white1.value)
    current_layout = links[current_layout].run(screen, screen_size)
    pygame.display.update()
