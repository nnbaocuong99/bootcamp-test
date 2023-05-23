{}, dict()

data = {
    "key": "value23",
    "status": True,
    "rollno": 23,
    "colors": ['red', 'green', 'blue']
}



print(type(data))
print(data['colors'])
print(data.get('colors', 20))


data['key'] = 'New Value'

print(len(data))
print(data.keys())
print(data.values())
print(data.items())

data['new_colors'] = ['brown']
data.update({'colors': ['brown']})
data.pop('colors')
data.popitem()

del data['colors']
del data

data.clear()
data_2 = data
data_3 = data.copy()
data_2['colors'] = ['brown']
data_3['colors'] = ['brown', 'green']

print(data)
print(data_2)
print(data_3)
print(data)

for key, value in data.items():
    # print(type(key))
    print(key, value)

for key in data.keys():
    # print(type(key))
    print(data[key])

for value in data.values():
    # print(type(key))
    print(value)

car = {
        "car": "BMW",
        "model":  2022
    }

data = {
    "key": "value23",
    "status": True,
    "rollno": 23,
    "colors": ['red', 'green', 'blue'],
    "models": car
}


print(car)
print(data)

data['models']['car'] = 'Mitsubishi'

print(car)
print(data)

colors = ('red', 'green', 'blue')
values = (12, 23,23)

print(dict.fromkeys(colors))
print(dict.fromkeys(colors, values))
print(data['models'])

a = 2
b = 5

if a < b: print('Greater')

print('Greater') if a > b else print('Wrong')

if (a > b) and (b == 0):
    print('RESULT')
    #return
#else:

print('wrong condition')

if (a > b):
    print('RESULT')
elif a == 2:
    print('a == 2')

def check(a, b):
    if (a > b) and (b == 0):
        return 'RESULT'
    return 'NO RESULT'
    
a = 10
b = 1

while a > b:
    b+=1
    if b == 4:
        continue
    print(b)

data = [1,2,3,4,5]
data = {
    "key": "value23",
    "status": True,
    "rollno": 23,
    "colors": ['red', 'green', 'blue'],
    "models": car
}

for x in data.items():
    print(x)


for x in range(len(data)):
    print(data[x])

# SELECT * data

#data = Person.objects.all()
#data = [object1, object2, object3...]

object.__dict__