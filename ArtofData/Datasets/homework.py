import csv

with open ("iris.csv", "r") as f:
    data = csv.DictReader(f, delimiter = ",")

    species = []
    sepal_width = []
    petal_length = []
    


    for line in data:
        if line:
            
            sepal = line[1]
            petal = line[2]

            sepal_width.append(sepal)
            petal_length.append(petal)


    print(species)
    print(sepal_width)
    print(petal_length)



