import pygame
from src.colors import color
from src import verticalButtonsDisplay, horizontalButtonDisplay
from src.blocks.rectangles import Rectangles
from src.ordination import algorithms
from src.ordination.algorithms import *


class Ordination:
    pygame.init()
    i = 0

    def __init__(self):
        self.header_box = pygame.Rect(30, 20, 580, 40)
        self.font = pygame.font.SysFont("montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
        self.font.set_bold(True)
        self.sort_algorithms = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Quicksort", "Merge Sort",
                                "Shell Sort", "Hybrid Sort"]
        self.buttons = ["Sort", "Stop", "Shuffle", "Info"]
        self.active = "Insertion Sort"
        self.action=""
        self.links = {0: algorithms.Insertion(), 1: algorithms.Selection(), 2: algorithms.Bubble(),
                      3: algorithms.Quick(), 4: algorithms.Merge(), 5: algorithms.Shell(), 6: algorithms.Hybrid()}
        self.sample = Rectangles()
        self.sort = False
        self.news = False
        self.spead_pos = (120, 325)
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

    def run(self, screen, screen_size):
        copyControl = self.action
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 30))

        self.mouse_pos = pygame.mouse.get_pos()

        # drawing the buttons 
        sort_spead = self.speadControl(screen)
        print(sort_spead)
        self.active = verticalButtonsDisplay(screen,self.sort_algorithms, 70, (420, 80),(190, 40), self.mouse_pos,self.active, self.font, self.sort)
        self.action = horizontalButtonDisplay(screen, self.buttons,  350, (30, 340), (90, 40), self.mouse_pos, self.action, self.font)
        if copyControl != self.action:
            self.stateControl() 
        self.sample.drawGrafic(screen)
        

        # checking when the buttons of are pressed
        if self.sort:
            mi, mx = self.links[self.sort_algorithms.index(self.active)].run(self.sample.get_hight_values())
            self.sample.swap_elements(mi, mx, screen, sort_spead)

        if self.news:
            self.sample.create_sample()
            self.news = False
            self.sorted = False

        return "ordination_algorithms"
    
    def speadControl(self, screen):
        pressed = False
        pygame.draw.line(screen, color.grey.value, (40, 325), (395, 325), 1)
        
        if self.mouse_pos[0] in range(40, 395) and self.mouse_pos[1] in range(305, 335):
            if pygame.mouse.get_pressed()[0]:
                self.spead_pos = (self.mouse_pos[0], 325)
                pressed = True
        pygame.draw.circle(screen, color.green.value, self.spead_pos, 10) if pressed else pygame.draw.circle(screen, color.white1.value, self.spead_pos, 10) 
        
        # 100÷355 = spead÷self.spead_pos[0]
        # spead = (100÷355)*self.spead_pos[0]
        return (3645/355)*self.spead_pos[0]