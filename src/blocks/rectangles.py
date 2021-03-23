import random
import pygame
from src.colors import color


class Rectangle:
    def __init__(self, x, widht):
        self.color = (255, 0, 0)
        self.widht = widht
        self.hight = random.randint(1, 10) * 20
        self.y = 305 - self.hight
        self.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.hight))


class Rectangles:
    sample = [Rectangle(25 * i + 45, 20) for i in range(14)]
    swap_indx1 = None
    swap_indx2 = None

    def __init__(self):
        self.sorted_sample = sorted(self.get_hight_values())

    def create_sample(self, sample_size):
        x = int(350 / (sample_size + 5) + 2)
        ajust = (x - sample_size) / 2
        if ajust < 0:
            ajust = ajust*-1
        # print(x, sampleSize, ajust)
        self.sample = [Rectangle((x+5) * i + (45-ajust), x) for i in range(int(sample_size / 2) + 7)]
        self.sorted_sample = sorted(self.get_hight_values())
        for i in range(len(self.sample)):
            self.set_right_color_to(i)

    def get_hight_values(self):
        return [elem.hight for elem in self.sample]

    def print_x_values(self):
        print([element.x for element in self.sample])

    def drawGrafic(self, screen):
        x, y = 30, 90
        x1, y1 = 417, 305
        pygame.draw.rect(screen, color.black.value, (40, 65, 370, 250))
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
        if self.sample[index].hight - self.sorted_sample[index] == 0:
            self.sample[index].color = color.green.value
        else:
            self.sample[index].color = color.red.value
    
    def is_sorted(self):
        for element in self.sample:
            if element.color == color.red.value:
                return False
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
                self.drawGrafic(screen)
            count+=0.01
        self.sample[index2], self.sample[index1] = self.sample[index1], self.sample[index2]
        self.set_right_color_to(index1)
        self.set_right_color_to(index2)
