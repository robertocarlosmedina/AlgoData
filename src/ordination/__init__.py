import pygame
import random
from pygame.locals import *
from src.colors import color
from src import verticalButtonsDisplay, horizontalButtonDisplay
from src.ordination import algorithms
from src.sample import Sample
from src.ordination.algorithms import *

class Ordination():
    pygame.init()
    def __init__(self):
        self.header_box = pygame.Rect(30, 20,580 , 40)
        self.font = pygame.font.SysFont("montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
        self.font.set_bold(True)
        self.sort_algorithms = ["Insertion Sort","Selection Sort", "Bubble Sort","Quicksort", "Merge Sort","Shell Sort", "Hybrid Sort"]
        self.actionButtons = ["Sort", "Stop", "News","Info"]
        self.active = self.sort_algorithms[0]
        self.action=""
        self.links = {"insertion": algorithms.Insertition(), "selection":algorithms.Selection(), 
                      "bubble":algorithms.Bubble(), "quick":algorithms.Quick(), "merge":algorithms.Merge(), 
                      "shell":algorithms.Shell(), "hybrid":algorithms.Hybrid()} # this is the Links to the algorithms
        # self.items = [2,3, 2, 4, 5, 6,4,4,2,1,3, 10,1,4] # max items = 14
        self.posiblePositions = [45,70,95,120,145,170,195,220,245,270,295,320,345,370]
        self.sampleSize = [random.randint(1, 10)for i in range(14)]
        self.items = [Sample(ssize, (pos_x, 305-(20*ssize))) for ssize, pos_x in zip(self.sampleSize, self.posiblePositions)]
        self.sort = False
        self.news = False
        self.pos = 0
        self.mouse_pos = ()
    
    def stateControl(self):
        if(self.action == "Sort"):
            self.sort = True
        elif(self.action == "News"):
            self.news = True
            self.sort = False
        else:
            self.sort = False
            self.news = False

    def drawGrafic(self, screen):
        x, y = 30, 90
        x1, y1 = 405, 305
        pos = 0
        pygame.draw.line(screen, color.grey.value, (x, y), (x, y1),3)
        pygame.draw.line(screen, color.grey.value, (x, y1), (x1, y1),3)

        for i in range(10):
            y1 -=20
            pygame.draw.line(screen, color.grey1.value, (x+3, y1), (x1, y1),1)
        x=45  
        y1 = 305
    
    def run(self,screen, screen_size):
        copyControl = self.action
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 30))

        self.mouse_pos = pygame.mouse.get_pos()

        # drawing the buttons 
        self.active = verticalButtonsDisplay(screen,self.sort_algorithms, 70, (420, 80),(190, 40), self.mouse_pos,self.active, self.font, self.sort)
        self.action = horizontalButtonDisplay(screen, self.actionButtons,  350, (30, 340), (90, 40), self.mouse_pos, self.action, self.font)
        if copyControl != self.action:
            self.stateControl() 

        # checking when the buttons of are pressed
        ids = [sample.id for sample in self.items]
        if self.sort:
            items = [self.links[key].run(ids) for key in self.links.keys() if self.active.split(" ")[0].lower() == key]
            self.items = items[0][0]
            self.pos = items[0][1]

        if self.news:
            self.items = []
            self.sampleSize = [random.randint(1, 10)for i in range(14)]
            self.items = [Sample(ssize, (pos_x, 305-(20*ssize))) for ssize, pos_x in zip(self.sampleSize, self.posiblePositions)]
            self.news = False
            self.pos = 0
            self.sorted = False
        self.drawGrafic(screen)
        return "ordination_algorithms"
        