import random
import pygame
from src.colors import color


class Rectangle:
    def __init__(self, x, widht):
        self.color = (255, 0, 0)
        self.widht = widht
        self.height = random.randint(1, 10) * 20
        self.y = 305 - self.height
        self.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.height))


class Rectangles:
    sample = [Rectangle(25 * i + 45, 20) for i in range(14)]
    swap_indx1 = None
    swap_indx2 = None
    already_sorted = False

    def __init__(self):
        self.sorted_sample = sorted(self.get_height_values())

    def create_sample(self, sample_size):
        aux = 402-((sample_size-1)*5)
        x = aux/sample_size
        # print(sample_size, aux, x)
        x_center = (680/2-((x+5) * sample_size + 45)/2)-82  # this is for center the sample in the graphic
        self.sample = [Rectangle((x+5) * i + x_center, x) for i in range(sample_size)]       
        self.sorted_sample = sorted(self.get_height_values())
        for i in range(len(self.sample)):
            self.set_right_color_to(i)
        self.already_sorted = False

    def get_height_values(self):
        return [elem.height for elem in self.sample]

    def print_x_values(self):
        print([element.x for element in self.sample])

    def drawGraphic(self, screen):
        x, y = 30, 90
        x1, y1 = 432, 305
        pygame.draw.rect(screen, color.black.value, (30, 65, 410, 245))
        # pygame.draw.line(screen, color.grey.value, (x, y), (x, y1), 3)
        pygame.draw.line(screen, color.grey.value, (x, y1), (x1, y1), 3)

        for i in range(10):
            y1 -= 20
            pygame.draw.line(screen, color.grey1.value, (x + 3, y1), (x1, y1), 1)

        self.draw_sample(screen)
        pygame.display.update()

    def draw_sample(self, screen):
        for element in self.sample:
            element.draw(screen)

    def set_right_color_to(self, index):
        if self.sample[index].height - self.sorted_sample[index] == 0:
            self.sample[index].color = color.green.value
        else:
            self.sample[index].color = color.red.value
    
    def is_sorted(self):
        if self.already_sorted:
            return True
        for element in self.sample:
            if element.color == color.red.value:
                return False
        self.already_sorted = True
        return True

    def swap_elements(self, index1, index2, screen, sort_speed):
        if index1 is None:
            return True
        self.sample[index1].color = color.yellow.value
        self.sample[index2].color = color.blue.value
        expected_x_index1 = self.sample[index2].x
        expected_x_index2 = self.sample[index1].x
        count, reached1, reached2 = 0, False, False
        while True:
            if count >= sort_speed:
                if self.sample[index1].x < expected_x_index1:
                    self.sample[index1].x += 1
                else:
                    self.sample[index1].x = expected_x_index1
                    reached1 = True
                if self.sample[index2].x > expected_x_index2:
                    self.sample[index2].x -= 1
                else:
                    self.sample[index2].x = expected_x_index2
                    reached2 = True
                count = 0
                if reached1 and reached2:
                    break
                self.drawGraphic(screen)
            count+=0.01
        self.sample[index2], self.sample[index1] = self.sample[index1], self.sample[index2]
        self.set_right_color_to(index1)
        self.set_right_color_to(index2)
