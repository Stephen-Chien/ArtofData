class Bookstore:

    def __init__(self, in_store = [], in_line = []):
        self.in_store = in_store
        self.in_line = in_line

    def size(self):
        return len(self.items)

    def enqueue(self, person):
        self.items.insert(0,person)

    # ?/10      #?/25

    # Move people to the line first, and then when the line is full, move people to the store

    # If someone leaves the store, dequeue, and then call the same method

    # If the store and line are full, return none

    # F and B

    #Impolekment the queue class using two stakcs
    







