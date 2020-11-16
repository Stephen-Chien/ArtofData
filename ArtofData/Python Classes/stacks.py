class Stack:

    def __init__(self):
        self.items = []
        
    def push (self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def string(self):
        return str(self)

    

    



# Take a list, turn it into a stack, and then for that stack you pop it off and put it into a new list
# Parentheses - Iterate through the string, if you see a left parethenese, put it onto the stack, same for the right parethenese
# Have to check the order of them
# Two stacks to sort the list, you want to start with unsorted stack and then sorted stack
#Do some comparisions
#To build up a sorted list








