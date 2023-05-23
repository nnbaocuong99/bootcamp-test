import json

data = {
    "name": "Jahanzeb",
    "contact": 12312321,
    "address": "House 333, Street 222",
    "active_user": True,
    "address_2": None,
    "cars": {
        "model": ["BMW", "HONDA"]
    },
    "colors": ["RED", "GREEN"]
}

try: 
    json_data = json.dumps(data)
except Exception as e:
    raise Exception(e)
    print("ERROR")
else:
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
finally:
    print(json_data)

username = int(input('Enter username:'))
username = raw_input('Enter username')

print(username)
