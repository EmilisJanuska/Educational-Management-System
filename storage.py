import json

Data_File = 'students.json'

def load_data():
    try:
        with open(Data_File, 'r') as file:
            return json.load(file) 
    except FileNotFoundError:
        return []
        
def save_data(students):
    with open(Data_File, 'w') as file:
        json.dump(students, file, indent=4, sort_keys= True)
        