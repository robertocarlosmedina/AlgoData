import pygame 
from pygame import *

screen_size = (640, 420)
colors = {"blue":(0, 0, 255), "white":(255, 255, 255), "green":(0, 255, 0), "black":(35,35,35)}
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('AlgoDataStuct')

def start():

    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["green"], pygame.Rect(0, 0, 40, 40))
    pygame.draw.rect(screen, colors["blue"], pygame.Rect(320, 0, 40, 40))
    pygame.draw.rect(screen, colors["blue"], pygame.Rect(0, 210, 40, 40))
    pygame.draw.rect(screen, colors["green"], pygame.Rect(320, 210, 40, 40))

keep_going = True

while keep_going:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    start()
    
    pygame.display.update()