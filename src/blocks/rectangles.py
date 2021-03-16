import random
import pygame


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
    sample = [Rectangle(25*i+45) for i in range(14)]
    # print(sample[1].hight, sample[2].hight, sep="  ")

    def create_sample(self):
        self.sample = [Rectangle(25*i+45) for i in range(14)]

    def print_hight_values(self):
        print([element.hight for element in self.sample])

    def print_x_values(self):
        print([element.x for element in self.sample])

    def draw_sample(self, pos, screen):
        for element in self.sample:
            if element.x > pos:
                element.color = (255, 0, 0)
            else:
                element.color = (0, 255, 0)
            element.draw(screen)

    def swap_elements(self, index1, index2):
        pass
