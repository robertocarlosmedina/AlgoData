import pygame
from src.blocks.rectangles import Rectangles
from src.colors import color
from src.ordination import algorithms
from src.ordination.algorithms import *


class Ordination:
    pygame.init()

    def __init__(self):
        self.header_box = pygame.Rect(30, 20, 580, 40)
        self.font = pygame.font.SysFont("montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
        self.font.set_bold(True)
        self.sort_algorithms = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Quicksort", "Merge Sort",
                                "Shell Sort", "Hybrid Sort"]
        self.Buttons = ["Sort", "Stop", "Shuffle", "Info"]
        self.active = 0
        self.action=""
        self.links = {0: algorithms.Insertion(), 1: algorithms.Selection(), 2: algorithms.Bubble(),
                      3: algorithms.Quick(), 4: algorithms.Merge(), 5: algorithms.Shell(), 6: algorithms.Hybrid()}
        self.sample = Rectangles()
        self.sort = False
        self.news = False
        self.pos = 0
        self.mouse_pos = ()

    def algorithmsButtonsDisplay(self, screen):
        y = 70  # for the boxes
        x1, y1, = 420, 80  # for the boxes texts
        box_dim=(190, 40)  # dimension of the boxes
        
        for algorithm in self.sort_algorithms:
            size = pygame.font.Font.size(self.font, algorithm)
            button_box = pygame.Rect(x1, y, box_dim[0], box_dim[1])

            # checking if the algorithms choice
            click = pygame.mouse.get_pressed()
            if self.mouse_pos[0]in range(x1, x1+box_dim[0]) and self.mouse_pos[1] in range(y1, y1+box_dim[1])\
                    and click[0] == 1 and not self.sort:
                self.active = self.sort_algorithms.index(algorithm)

            # hover button effect
            if self.mouse_pos[0]in range(x1, x1+box_dim[0]) and self.mouse_pos[1] in range(y1, y1+box_dim[1]):
                pygame.draw.rect(screen, color.grey.value, button_box)
                line = self.font.render(algorithm, True, color.white.value)
            else:
                pygame.draw.rect(screen, color.grey.value, button_box, 2)
                line = self.font.render(algorithm, True, color.white.value)
            
            if self.active == self.sort_algorithms.index(algorithm):
                pygame.draw.rect(screen, color.green.value, button_box)
                line = self.font.render(algorithm, True, color.black.value)

            screen.blit(line, (x1-(size[0]/2)+(box_dim[0]/2), y1))
            y += 45
            y1 += 45  
    
    def ButtonDisplay(self, screen):
        y = 350  # for the boxes text's
        x1, y1 = 30, 340  # for the boxes texts
        box_dim=(90, 40)  # dimension of the boxes
        for button in self.Buttons:
            size = pygame.font.Font.size(self.font, button)
            button_box = pygame.Rect(x1, y1, box_dim[0], box_dim[1])

            # checking if the algorithms choice
            click = pygame.mouse.get_pressed()
            if self.mouse_pos[0]in range(x1,x1+box_dim[0]) and self.mouse_pos[1]\
                    in range(y1, y1+box_dim[1]) and click[0] == 1:
                self.action = button
                self.stateControl()

            # hover button effect
            if self.mouse_pos[0]in range(x1, x1+box_dim[0]) and self.mouse_pos[1] in range(y1, y1+box_dim[1]):
                pygame.draw.rect(screen, color.grey.value, button_box)
                line = self.font.render(button, True, color.white.value)
            else:
                pygame.draw.rect(screen, color.grey.value, button_box, 2)
                line = self.font.render(button, True, color.white.value)
            
            if self.action == button:
                pygame.draw.rect(screen, color.blue.value, button_box)
                line = self.font.render(button, True, color.white.value)

            screen.blit(line, (x1-(size[0]/2)+(box_dim[0]/2), y))
            x1 += 95
    
    def stateControl(self):
        if self.action == self.Buttons[0]:
            self.sort = True
        elif self.action == self.Buttons[2]:
            self.news = True
            self.sort = False
        else:
            self.sort = False
            self.news = False

    def drawGrafic(self, screen):
        x, y = 30, 90
        x1, y1 = 405, 305
        pos = 0
        pygame.draw.line(screen, color.grey.value, (x, y), (x, y1), 3)
        pygame.draw.line(screen, color.grey.value, (x, y1), (x1, y1), 3)

        for i in range(10):
            y1 -=20
            pygame.draw.line(screen, color.grey1.value, (x+3, y1), (x1, y1), 1)
        x=45  
        
        self.sample.draw_sample(pos, screen)
    
    def run(self, screen, screen_size):
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 30))

        self.mouse_pos = pygame.mouse.get_pos()

        # drawing the buttons 
        self.algorithmsButtonsDisplay(screen)
        self.ButtonDisplay(screen)
        self.drawGrafic(screen)

        # checking when the buttons of are pressed
        if self.sort:
            returned = self.links[self.active].run(self.sample.sample)
            self.sample.sample = returned[0]
            self.pos = returned[1]
        if self.news:
            self.sample.create_sample()
            self.news = False
            self.pos = 0
            self.sorted = False

        return "ordination_algorithms"
