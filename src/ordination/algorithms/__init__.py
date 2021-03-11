import pygame
from src.colors import color

class Insertition():

    def run(self, screen, items):
        x, y = 45, 90
        x1, y1 = 405, 305
        for i in range(1, len(items)):
            x, y = 45, 90
            x1, y1 = 405, 305
            key = items[i]
            # Move elements of arr[0..i-1], that are greater than key
            # to one position ahead of their current position
            j = i-1
            while j >=0 and key < items[j] :
               items[j+1] = items[j]
               j -= 1
            items[j+1] = key
            
            for item in items:
                y1 = 305
                # print(item)
                for i in range(item):
                    y1-=20
                    item_box=pygame.Rect(x, y1, 20, 20)
                    pygame.draw.rect(screen, color.green.value, item_box)
                x+=25
        return items

class Selection():
    def run(self,screen, items):    
        print("selection")

class Bubble():
    def run(self, screen, items):
        print("bubble")

class Quick():
    def run(self, screen, items):   
        print("quick")

class Merge():
    def run(self, screen, items):
        print("merge")

class Shell():
    def run(self, screen, items):
        print("merge")

class Hybrid():
    def run(self, screen, items):
        print("hybrid")
