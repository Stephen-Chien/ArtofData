import csv

#function for adding all types of beds from different counties
def max(l):
  return sum(l)

'''
Go through each key of @d:dict,
find sum of the values of @category:String,
then return key with greatest bed number
'''

def get_max(d, category):
  # Keep track of current max
  cur_max = [None, None] # [key, val]

  for key in d:
    max_value = max(d[key][category])

    # Update current max
    if (cur_max[0] is None) or (max_value >= cur_max[1]):
      cur_max = [key, max_value]

  # String formatting
  print("Greatest {} - {}: {:.3f}".format(category, cur_max[0], cur_max[1]))
  return cur_max[0]

NY = {}
  
with open("/Users/stephen/Documents/GitHub/ArtofData/ArtofData/API_Project/cleanedset.csv", "r") as f:
    data = csv.reader(f)
    next(data) # skip labels line
    for row in data:
      county = row[2]

      if county not in NY: # Initialize dictionary if doesn't exist
        NY[county] = {'bed-per-person': []}

      NY[county]['bed-per-person'].append(float(row[5])/2000) #dividing by 2000 to get the approx. num of beds per person
      

  # Printing number of the beds
for county in NY:
    print(county)
    print("\tNumber of beds", max(NY[county]['bed-per-person']))
    

  # Find max

get_max(NY, 'bed-per-person')


