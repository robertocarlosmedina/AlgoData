
class Insertion:
    @staticmethod
    def run(items):
        sort = False
        for i in range(1, len(items)):
            key = items[i]
            # Move elements of arr[0..i-1], that are greater than key to one position ahead of their current position
            j = i-1
            while j >=0 and key < items[j] :
                items[j+1] = items[j]
                j -= 1
                sort = True
            items[j+1] = key
            if sort:
                return j+1,i
        return None, None
        
class Selection:
    @staticmethod
    def run(items): 
        sort = False  
        for i in range(len(items)):
            min_item = i # assuming that the first item ins the lowest 
            for j in range(i+1,len(items)):
                if items[j]<items[min_item]: # verify if if's one lower than min_item
                    min_item = j
                    sort = True
            if sort:
                return i, min_item
        return None, None

class Bubble:
    def run(self, screen, items):
        print("bubble")

class Quick:
    def run(self, screen, items):   
        print("quick")

class Merge:
    def run(self, screen, items):
        print("merge")

class Shell:
    def run(self, screen, items):
        print("merge")

class Hybrid:
    def run(self, screen, items):
        print("hybrid")
