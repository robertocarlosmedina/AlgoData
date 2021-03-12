import pygame
from src.colors import color

class Insertition():
    def __init__(self):
        self.count = 0
        self.sort = False
        self.pos = 0

    def run(self, items):
        self.sort = False
        if self.count >= 300:
            for i in range(1, len(items)):
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
        self.count+=1
        return items, self.pos

class Selection():
    def __init__(self):
        self.pos = self.count = 0
        self.sort = False

    def run(self, items):   
        self.sort = False
        if self.count >300:
            for i in range(len(items)):
                min_item = i # assuming that the first item ins the lowest 
                for j in range(i+1,len(items)):
                    if items[j]<items[min_item]: # verify if if's one lower than min_item
                        min_item = j
                        self.sort = True
                    self.pos=i
                items[i], items[min_item] = items[min_item], items[i] # change de positions
                if self.sort:
                    break
            self.count = 0
        self.count += 1
        return items, self.pos

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
