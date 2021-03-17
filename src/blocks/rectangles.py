import random
import pygame
from pygame.constants import K_s
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
    swap_indx1 = None
    swap_indx2 = None

    def __init__(self):
        self.sorted_sample = sorted(self.get_hight_values())

    def create_sample(self):
        self.sample = [Rectangle(25 * i + 45) for i in range(14)]

    def get_hight_values(self):
        return [elem.hight for elem in self.sample]

    def print_x_values(self):
        print([element.x for element in self.sample])

    def drawGrafic(self, screen):
        x, y = 30, 90
        x1, y1 = 405, 305
        pygame.draw.rect(screen, color.black.value, (40, 65, 370, 250))
        pygame.draw.line(screen, color.grey.value, (x, y), (x, y1), 3)
        pygame.draw.line(screen, color.grey.value, (x, y1), (x1, y1), 3)

        for i in range(10):
            y1 -= 20
            pygame.draw.line(screen, color.grey1.value, (x + 3, y1), (x1, y1), 1)

        self.draw_sample(screen)
        pygame.display.update()

    def draw_sample(self, screen):
        for element in self.sample:
            element.draw(screen)

    def swap_elements(self, index1, index2, screen, sort_spead):
        action = "Sort"
        if index1 is None:
            return True
        self.sample[index1].color = color.yellow.value
        self.sample[index2].color = color.blue.value
        espected_x_index1 = self.sample[index2].x
        espected_x_index2 = self.sample[index1].x
        count, reached1, reached2 = 300, False, False
        while True:
            if count >= sort_spead:
                if self.sample[index1].x < espected_x_index1:
                    self.sample[index1].x += 1
                else:
                    self.sample[index1].x = espected_x_index1
                    reached1 = True
                if self.sample[index2].x > espected_x_index2:
                    self.sample[index2].x -= 1
                else:
                    self.sample[index2].x = espected_x_index2
                    reached2 = True
                count = 0
                if reached1 and reached2:
                    break
                self.drawGrafic(screen)
            count+=0.01
        self.sample[index2], self.sample[index1] = self.sample[index1],self.sample[index2]
