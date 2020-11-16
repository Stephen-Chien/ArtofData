import csv



petal_length = [] # creating empty lists 
sepal_width = []

with open('iris.csv', 'r') as f:
	data = csv.reader(f)
	next(data)	#skips a row in data
	for row in data:
            if row: # I had an error here for the index, so I added this
				petal = float(row[2]) 
				petal_length.append(petal) #appending petal(the row of petal lengths) to petal length
				sepal = float(row[1])
				sepal_width.append(sepal) #doing the same for sepal width

def average(num):
    sum = 0
    for x in num:
        sum += x         

    avg = sum / len(num)
    return avg
  

print("The averages for petal length, in descending order from Setosa/Virsicolor/Virginica are: \n")

print(average(petal_length[0:52]))#average for iris-setosa petal length

print(average(petal_length[52:102]))#average for virsicolor

print(average(petal_length[102:152]))# average for virginica

print("")

print("The averages for sepal width, in descending order from Setosa/Virsicolor/Virginica are: \n")

print(average(sepal_width[0:52]))

print(average(sepal_width[52:102]))

print(average(sepal_width[102:152]))


print("")

print("So, Iris Virginica has the largest petal length, and Iris Setosa has the largest sepal width")





