class RingBuffer:
    def __init__(self, capacity):
        # set capacity limit
        self.capacity = capacity
        # set index
        self.index = 0
        # instantiate empty storage list
        self.storage = []

    def append(self, item):
        #if length of storage less than the capacity then append the item 
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # f the storage index is equal to that item then 
            self.storage[self.index] = item 
            #then increase index count by 1 
        self.index += 1

        #if index and capacity are equal set index to 0 
        if self.index == self.capacity:
            #setting index to 0 because 
            self.index = 0 

    def get(self):
        #return list 
        return self.storage
        