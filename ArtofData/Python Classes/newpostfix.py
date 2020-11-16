
import csv #Importing.csv and Stack file
from stacks import Stack


def evaluate(row):
    stack = [] # Creating a new list called Stack
    for a in row:
        if a in ['0','1','2','3','4','5','6','7','8','9','10']: #If there is a number, push it to the stack
            stack.append(a)
            continue

        num1, num2 = stack.pop(), stack.pop() #assigning the two last popped values to num1 and num2

        if a == '+': # All of the operations, if there is an operator, add/multiply/subtract the two popped numbers
            stack.append(int(num2) + int(num1)) 
        elif a == '-':
            stack.append(int(num2) - int(num1))
        elif a == '*':
            stack.append(int(num2) * int(num1))

    
       
    return stack.pop() # Whatever the last element gets returned



with open("calculate_me.csv", "r") as f: #Calling CSV Reader here to take in CSV File
    data  = csv.reader(f) 
    total = 0           
    total_of_evaluate = 0

    for row in data:   #For row in data, add the return of the function evaluate to total of evaluate, and add one to total
        total_of_evaluate += evaluate(row)
        total += 1
    
    print(total_of_evaluate/total) # Average of all of the rows

        





        
        
    


    


        
