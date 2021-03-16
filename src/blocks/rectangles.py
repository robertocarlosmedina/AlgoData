import random
import pygame
from src.colors import color


class Rectangle:
    def __init__(self, x):
        self.color = (255, 0, 0)
        self.widht = 20
        self.hight = random.randint(1, 10) * 20
        self.y = 305 - self.hight
        self.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.hight))


class Rectangles:
    sample = [Rectangle(25 * i + 45) for i in range(14)]
    sorted_sample = sorted(sample)
    swap_indx1 = None
    swap_indx2 = None

    # print(sample[1].hight, sample[2].hight, sep="  ")

    def create_sample(self):
        self.sample = [Rectangle(25 * i + 45) for i in range(14)]

    def get_hight_values(self):
        return [elem.hight for elem in self.sample]

    def print_x_values(self):
        print([element.x for element in self.sample])

    def drawGrafic(self, screen):
        x, y = 30, 90
        x1, y1 = 405, 305
        pos = 0
        pygame.draw.line(screen, color.grey.value, (x, y), (x, y1), 3)
        pygame.draw.line(screen, color.grey.value, (x, y1), (x1, y1), 3)

        for i in range(10):
            y1 -= 20
            pygame.draw.line(screen, color.grey1.value, (x + 3, y1), (x1, y1), 1)

        self.draw_sample(pos, screen)

    def draw_sample(self, pos, screen):
        for element in self.sample:
            if element.x > pos:
                element.color = (255, 0, 0)
            else:
                element.color = (0, 255, 0)
            element.draw(screen)

    def swap_elements(self, index1, index2):

        while index2 != self.swap_indx2 and index1 != self.swap_indx1:

