import csv
from stacks import Stack



def operator(sign, one, two):
    if sign == "*":
        result = one * two
    elif sign == "+":
        result = one + two
    elif sign == "-":
       result = one - two
    
    return result

def evaluate(row):
    stack = Stack()
    total = 0
           
    for i in range(len(row)):   
        if i in ("*", "+", "-"):
            one = stack.pop()
            two = stack.pop()
            total += operator(sign, one, two)
            stack.push(total)
        else:
            stack.push(row[i])

    return stack.string()


with open("calculate.csv", "r") as f:
    data  = csv.reader(f) 
    for row in data:
        print(row)
        print(evaluate(row))
       
        








    


