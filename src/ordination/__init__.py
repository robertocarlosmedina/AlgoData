import pygame
from src import verticalButtonsDisplay, horizontalButtonDisplay
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
        self.buttons = ["Sort", "Stop", "Shuffle", "Info"]
        self.active = 0
        self.action=""
        self.links = {0: algorithms.Insertion(), 1: algorithms.Selection(), 2: algorithms.Bubble(),
                      3: algorithms.Quick(), 4: algorithms.Merge(), 5: algorithms.Shell(), 6: algorithms.Hybrid()}
        self.sample = Rectangles()
        self.sort = False
        self.news = False
        self.pos = 0
        self.mouse_pos = ()
    
    def stateControl(self):
        if self.action == self.buttons[0]:
            self.sort = True
        elif self.action == self.buttons[2]:
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
        copyControl = self.action
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 30))

        self.mouse_pos = pygame.mouse.get_pos()

        # drawing the buttons 
        self.active = verticalButtonsDisplay(screen,self.sort_algorithms, 70, (420, 80),(190, 40), self.mouse_pos,self.active, self.font, self.sort)
        self.action = horizontalButtonDisplay(screen, self.buttons,  350, (30, 340), (90, 40), self.mouse_pos, self.action, self.font)
        if copyControl != self.action:
            self.stateControl() 
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