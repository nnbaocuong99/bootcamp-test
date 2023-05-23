
dict  == object 
list == array 
tuple == array 
str == string 
int == Number 
True  == true 
False == false 
None == null 

import json 

data = {
    "name": "James",
    "contact": 12312321,
    "address": "House 1, Street 123",
    "active_user": True,
    "address_2": None,
    "cars": {
        "model": ["BMW", "HONDA"]
    },
    "colors": ["RED", "GREEN"]
}

json_data = json.dumps(data, indent=4)

print(type(json_data))
print(json_data)

json_data = json.dump()
python_dict = json.loads(json_data)

print(type(python_dict))
print(python_dict)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    file_data = json.load(file)


print(file_data['name'])