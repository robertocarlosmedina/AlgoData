import pygame
from src.colors import color

class Insertition():
    def __init__(self):
        self.count = 0
        self.sort = False
        self.pos = 0

    def run(self, screen, items):
        self.sort = False
        copy = items
        if self.count >= 300:
            for i in range(1, len(items)):
                x, y = 45, 90
                x1, y1 = 405, 305
                key = items[i]
                # Move elements of arr[0..i-1], that are greater than key
                # to one position ahead of their current position
                self.pos = j = i-1
                while j >=0 and key < items[j] :
                   items[j+1] = items[j]
                   j -= 1
                   self.sort = True
                items[j+1] = key

                if self.sort:
                    break
            self.count = 0
        else:
            self.count+=1

        return items, self.pos
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
