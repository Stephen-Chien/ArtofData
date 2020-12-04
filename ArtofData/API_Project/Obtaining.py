import requests


base_url = "https://hm-cs.herokuapp.com"
endpoint = "/hospital"
key = "ArtOfDataKEY123"

#boolean and variable to continue while loop
ifTrue = True 
x = 0

def query(id):
        payload = { 
                "key" : key,
                "id" : id #the id, retrieves the “id”th row of the dataset
        }

        # taking in the key and the rows, this is what we want from the computer
        response = requests.get(base_url + endpoint, params = payload)

        if response.status_code == requests.codes.ok: #If we get a response, print the data and return true
                data = response.text
                print(data)
                return True

        else:
                print(response.status_code) #Print the error code if there is one
                print(response.text)
                return False


while ifTrue:
        ifTrue = query(x)
        x += 1
