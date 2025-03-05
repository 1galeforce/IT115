import json # Import class library


# Create data structure dictionary for json

data1 = {

    'name':'OJ Simpson',
    'age':30,
    'city': 'New York, NY',
    'interests':['Traveling', 'Football', 'Golf', 'Running', 'Videogames', 'History'],
    'is_student': True
  
}

#Creating a Json file and writing the python object contents to the json_file
with open('data1.json','w') as json_file:  

     #Dump the Data Dictionary into the JSON file       
    json.dump(data1,json_file,indent=4) #data1 indicates where the dictionary is located; created the json_ file in the folder

print("You have successfully written to data1.json") #a print statement on line 20 makes sure that line 18 is executed.



