import pygame
from src.colors import color, rgbColor


class Start:
    pygame.init()
    y1, x1 = None, None

    def __init__(self):
        self.size = 60
        self.box_info = []
        self.x, self.y = 260, 150
        self.changeColor = True
        self.font = pygame.font.Font("montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
        self.timer = 0

    def run(self, screen, screen_size):
        self.box_info = []
        self.x1, self.y1 = self.x, self.y
        if self.size>4:
            if self.timer >= 250:
                self.changeColor = not self.changeColor
                self.timer = 0
            else:
                self.timer +=1
            for i in range(2):
                for f in range(2):
                    self.box_info.append(((self.x1, self.y1), "green")) if self.changeColor else self.box_info.append((
                        (self.x1, self.y1), "blue"))
                    self.x1+=60
                    self.changeColor = not self.changeColor
                self.changeColor = not self.changeColor
                self.x1 = self.x
                self.y1+=60
            [pygame.draw.rect(screen, rgbColor(info[1]), pygame.Rect(info[0][0], info[0][1], self.size, self.size))
             for info in self.box_info]
            self.size -= 0.02
            self.x += 0.01
            self.y += 0.01
            size = pygame.font.Font.size(self.font, 'AlgorDataStruct')
            line = self.font.render('AlgorDataStruct', True, color.white.value)
            screen.blit(line, (screen_size[0]/2-size[0]/2, screen_size[1]/2-size[1]/2))
            return "start"
        else:
            return "ordination_algorithms"
