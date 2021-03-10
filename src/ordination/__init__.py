import pygame
from pygame.locals import *
from src.colors import color, rgbColor

class Ordination():
    pygame.init()
    def __init__(self):
        self.header_box = pygame.Rect(30, 20,580 , 40)
        self.font = pygame.font.SysFont("arial", 20)
        self.font.set_bold(True)
        self.sort_algorithms = ["Insertion Sort","Selection Sort", "Bubble Sort","Quicksort", "Merge Sort","Shell Sort", "Hybrid Sort"]
        self.active = self.sort_algorithms[0]
        
    def buttonsDisplay(self, screen):
        y = 70
        x1, y1, = 430, 80
        box_dim=(190, 40)
        
        for algorithm in self.sort_algorithms:
            mouse_pos = pygame.mouse.get_pos()
            size = pygame.font.Font.size(self.font, algorithm)
            button_box = pygame.Rect(420, y, box_dim[0], box_dim[1])
            if(self.active == algorithm):
                pygame.draw.rect(screen, color.green.value, button_box)
                line = self.font.render(algorithm, True, color.black.value)
            else:
                pygame.draw.rect(screen, color.grey.value, button_box, 2)
                line = self.font.render(algorithm, True, color.white.value)
            
            # checking if the algorithms choice
            click = pygame.mouse.get_pressed()
            if mouse_pos[0]in range(x1,x1+box_dim[0]) and mouse_pos[1] in range(y1,y1+box_dim[1]) and click[0] == 1:
                self.active = algorithm

            screen.blit(line, (x1, y1))
            y += 45
            y1 += 45
        
    
    def run(self,screen, screen_size):
        screen.fill(color.black.value)
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 27))

        # drawing the buttons 
        self.buttonsDisplay(screen)
        return "ordination_algorithms"
        