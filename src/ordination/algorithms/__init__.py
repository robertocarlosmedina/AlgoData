# ___________________________Descripton__________________________

# The following implemted some of the sort algorithms for the need 
# of visual perception of the algorithms to the app the class have 
# a special form of implementation, but all of them had a same 
# commun thing, that is the return of their run() method, that will 
# be the index value of the a minimo and the index value of a maximo
# to be changed.

class Insertion:
    @staticmethod
    def run(items, useless):
        sort = False
        for i in range(1, len(items)):
            key = items[i]
            # Move elements of arr[0..i-1], that are greater than key to one position ahead of their current position
            j = i-1
            while j >=0 and key < items[j]:
                items[j+1] = items[j]
                j -= 1
                sort = True
            items[j+1] = key
            if sort:
                return j+1, i
        return None, None

class Selection:
    @staticmethod
    def run(items, useless):
        sort = False  
        for i in range(len(items)):
            min_item = i  # assuming that the first item ins the lowest
            for j in range(i+1, len(items)):
                if items[j]<items[min_item]:  # verify if if's one lower than min_item
                    min_item = j
                    sort = True
            if sort:
                return i, min_item
        return None, None

class Bubble:
    index = 0
    all_index_change = []
    pos_last_index_returned = 0  # to control the positions index to make the changes
    def run(self, items, useless):
        
        if useless:
            self.all_index_change=[]
            self.pos_last_index_returned = 0
            while True:
                sort = False
                for passnum in range(len(items)-1,0,-1):
                    for i in range(passnum):
                        if items[i]>items[i+1]:
                            temp = items[i]
                            items[i] = items[i+1]
                            items[i+1] = temp
                            self.all_index_change.append((i, i+1))
                            sort = True              

                if not sort:
                    break
                self.index = 0

        i = 0
        for index in self.all_index_change:
            if i == self.pos_last_index_returned:
                self.pos_last_index_returned += 1
                return index[0], index[1]
            i += 1
        return None, None

class Quick:
    pos_last_index_returned = 0  # to control the positions index to make the changes
    index = []  # to store all the index made by the sort
    def filtring(self):
        i = 0
        for elm in self.index:
            if elm[0] == elm[1]:
                self.index.pop(i)
            i += 1


    def run(self, items, new_sample):
        # to control if the sample sent is a new one
        # if the sample is a new one this will do the sort using this algorithms
        # and reset all the control variable
        if new_sample:
            low, high = 0, len(items) - 1
            self.index = []
            self.pos_last_index_returned = 0
            mx = self.quicksort(items, low, high)
            del mx

        # This is to control the index that will be sent, keeping in mind 
        # the one's that was already sent
        self.filtring()
        i = 0
        for index in self.index:
            if i == self.pos_last_index_returned:
                self.pos_last_index_returned += 1
                if index[0]>index[1]:
                    return index[1],index[0]
                return index[0], index[1]
            i += 1
        return None, None
        
    def quicksort(self, items, low, high):
        if len(items)==1:
            return items
        if low<high:
            #  p is the partition index
            p = self.partition(items, low, high)

            self.quicksort(items, low, p-1)  # view all the one's that are lower than the partition index
            self.quicksort(items, p+1, high)  # view all the one's that are higher than the partition index

    def partition(self, items, low, high):
        pivot = items[high]  # owner pivot
        i = low-1  # index position of the smaller element

        for j in range(low, high):  # an iteration from the low one to the high one
            if items[j]<=pivot:  # checking all the one's that are lower than the pivot
                i = i+1
                self.index.append((j, i))  # Storing the index
                items[i], items[j]=items[j], items[i]  # swapping the elements
        self.index.append((i+1, high))  # Storing the index
        items[i+1], items[high] = items[high], items[i+1]  # swapping the elements
        return i+1

class Merge:
    def run(self, items, new_sample):
        print("merge")

class Shell:
    all_index_change = []
    pos_last_index_returned = 0  # to control the positions index to make the changes

    def run(self, items, new_sample):
        if new_sample:
            self.all_index_change = []
            self.pos_last_index_returned = 0
            index_interval = len(items)//2
            while index_interval > 0:
                for i in range(index_interval, len(items)):
                    item = items[i]
                    j = i
                    while j >= index_interval and items[j - index_interval] > item:
                        items[j] = items[j - index_interval]
                        self.all_index_change.append(( j - index_interval, j))
                        j -= index_interval
                    items[j] = item
                index_interval = index_interval//2
        
        i = 0
        for index in self.all_index_change:
            if i == self.pos_last_index_returned:
                self.pos_last_index_returned += 1
                return index[0], index[1]
            i += 1
        return None, None
        # print(self.all_index_change)

class Heap:
    all_index_change = []
    pos_last_index_returned = 0  # to control the positions index to make the changes
    def run(self, items, new_sample):
        n = len(items)

        if new_sample:
            # Build a maxheap.
            # Since last parent will be at ((n//2)-1) we can start at that location.
            for i in range(n // 2 - 1, -1, -1):
                self.heapify(items, n, i)

            # One by one extract elements
            for i in range(n-1, 0, -1):
                items[i], items[0] = items[0], items[i]   # swap
                self.all_index_change.append((0,i))
                self.heapify(items, i, 0)

        # if the index that will be change in the sort hare already determinated
        i = 0
        for index in self.all_index_change:
            if i == self.pos_last_index_returned:
                self.pos_last_index_returned += 1
                return index[0], index[1]
            i += 1
        return None, None

    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self,arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            self.all_index_change.append((i, largest))
            arr[i],arr[largest] = arr[largest],arr[i]  # swap
    
            # Heapify the root.
            self.heapify(arr, n, largest)
    

# ___________________________Testing aria__________________________


# shell = Bubble()
# array = [12, 134, 22, 323,1 ,31,3, 13, 23, 2,3, 1, 346, 7]
# new = True
# while True:
#     mi, mx = shell.run(array, new)
#     new = False
#     if mi == None:
#         break
#     else:
#         print(mi, mx)
        
#         array[mi], array[mx] = array[mi], array[mx]
#         # print(array)
#     print(array)

