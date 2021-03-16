import pygame
from src.colors import color

class Sample():
    def __init__(self, id, initial_pos):
        self.id = id
        self.pos = initial_pos
    def draw(self, screen, pos):
        item_box=pygame.Rect(self.pos[0], self.pos[1]-(self.id*20), 20, 20*self.id)
        pygame.draw.rect(screen, color.green.value, item_box) if pos < self.pos or self.pos >= len(self.items)-2 else pygame.draw.rect(screen, color.red.value, item_box)
        
    def move(self):
        pass