import pygame
from src.colors import color, rgbColor

class Ordination():
    pygame.init()
    def __init__(self):
        self.header_box = pygame.Rect(30, 20,580 , 40)
        self.font = pygame.font.Font("montserrat-font/MontserratMedium-nRxlJ.ttf", 20)
        self.font.set_bold(True)
        self.sort_algorithms = ["Insertion Sort","Selection Sort", "Bubble Sort","Quicksort", "Merge Sort","Shell Sort", "Hybrid Sort"]
        self.active = self.sort_algorithms[0]
    
    def buttonsDisplay(self, screen):
        y = 70
        x1, y1, = 430, 77
        for algorithm in self.sort_algorithms:
            button_box = pygame.Rect(420, y, 190, 40)
            if(self.active == algorithm):
                pygame.draw.rect(screen, color.green.value, button_box)
                line = self.font.render(algorithm, True, color.black.value)
            else:
                pygame.draw.rect(screen, color.grey.value, button_box, 2)
                line = self.font.render(algorithm, True, color.white.value)

            # size = pygame.font.Font.size(self.font, algorithm)
            screen.blit(line, (x1, y1))
            y += 45
            y1 += 45
    
    def run(self,screen, screen_size):
        screen.fill(color.black.value)
        pygame.draw.rect(screen, color.grey.value, self.header_box, 2)
        size = pygame.font.Font.size(self.font, 'Sorting algorithms ')
        self.font.set_bold(True)
        line = self.font.render('Sorting algorithms ', True, color.white.value)
        screen.blit(line, (screen_size[0]/2-size[0]/2, 27))

        # drawing the buttons 
        self.buttonsDisplay(screen)
        return "ordination_algorithms"
        