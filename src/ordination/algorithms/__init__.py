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

    def run(self, items, useless):
        sort = False
        if not useless:
            for i in range(self.index, len(items)-1):
                if items[i]>items[i+1]:
                    sort, mi, mx, self.index = True, i, i+1, i
                if sort:
                    return mi, mx
                self.index = 0
        return None, None


class Quick:
    pos_las_index_returned = 0  # to control the positions index to make the changes
    index = []  # to store all the index made by the sort

    def run(self, items, new_sample):
        # to control if the sample sent is a new one
        # if the sample is a new one this will do the sort using this algorithms
        # and reset all the control variable
        if new_sample:
            low, high = 0, len(items) - 1
            self.index = []
            self.pos_las_index_returned = 0
            mx = self.quicksort(items, low, high)
            del mx

        # This is to control the index that will be sent, keeping in mind 
        # the one's that was already sent
        i = 0
        for index in self.index:
            if i == self.pos_las_index_returned:
                self.pos_las_index_returned += 1
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
                self.index.append((i, j))  # Storing the index
                items[i], items[j]=items[j], items[i]  # swapping the elements
        self.index.append((i+1, high))  # Storing the index
        items[i+1], items[high] = items[high], items[i+1]  # swapping the elements
        return i+1


class Merge:
    def run(self, items, new_sample):
        print("merge")

class Shell:
    def run(self, items, new_sample):
        print("merge")

class Hybrid:
    def run(self, items, new_sample):
        print("hybrid")
