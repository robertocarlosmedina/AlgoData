def read_last_index(items):
    file = open("extra_values.txt", "r")
    line = file.readline()
    if line == "":
        last_index = 0
    else:
        last_index = int(line)
        if last_index == len(items)-1:
            last_index = 0
    file.close()
    return last_index


def write_last_index(index, items):
    if index == len(items)-1:
        index = 0
    file = open("extra_values.txt", "w")
    file.write(str(index+1))
    file.close()


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
    @staticmethod
    def run(items):
        last_index = read_last_index(items)
        for i in range(last_index, len(items)-1):
            write_last_index(i, items)
            if items[i]>items[i+1]:
                return i, i+1
        return None, None

class Quick:
    sort = False
    def run(self, items):
        low, high = 0, len(items)-1
        mi, mx = self.quicksort(items, low, high)
        return mi, mx
        
    def quicksort(self,items, low, high):
        self.sort = False
        if len(items)==1:
            return None, None
        if low<high:
            #  p is the partition index
            p = self.partition(items, low, high)
            if self.sort:
                return p-1, p+1

            self.quicksort(items, low, p-1)
            self.quicksort(items, p+1, high)

    def partition(self, items, low, high):
        pivot = items[high] # ower pivot
        i = low-1 # index position of the smaller element

        for j in range(low, high):
            if items[j]<=pivot:
                i = i+1
                self.sort = True
                items[i], items[j]=items[j], items[i]

        items[i+1], items[high] = items[high], items[i+1] 
        return i+1

class Merge:
    def run(self, screen, items):
        print("merge")

class Shell:
    def run(self, screen, items):
        print("merge")

class Hybrid:
    def run(self, screen, items):
        print("hybrid")


# array = [2,245, 656, 45,4,3,4,7,8,823,2]
# sort = Quick()

# while True:
#     mi, mx = sort.run(array)
#     print(mi, mx)
#     if mi != None:
#         array[mi], array[mx] = array[mx], array[mi]
#         print (array)
#     else:
#         break
    
# print (array)

  