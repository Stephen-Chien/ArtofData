import csv


with open("ArtofData/API_Project/hospitalset.csv", 'r') as f:
    data = csv.reader(f) # reading in the rows
    next(data) #skipping the titles
    for row in data:
            if row[4] == "500HAB":
                row[5] = float(row[5]) * 4 #Multiply beds by 4 because instead of 500 ppl, there are 200ppl
                row[4] = "2000HAB"
                print(row)
            elif row[4] == "1000HAB": #Multiply by 2
                row[5] = float(row[5]) * 2
                row[4] = "2000HAB"
                print(row)
            elif row[4] == "2000HAB": #Print same result
                print(row)
                #printing all of the rows to generated a cleaned CSV File
          



               




    
                