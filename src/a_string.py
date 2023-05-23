
data = "Hello check=True"
data = "Hello World!"

print(type(data))
print(len(data))
print(data[1])

for alpha in data:
     print(alpha)

print("WD" in data)
print("WD" not in data)

if 'WD' not in data:
     print('This value is not in the string.')

print(type(data[-4:]))
print(type(bool(data[-4:])))
print(data.upper())
print(data.lower())
print(data.capitalize())

data = " Hello "
print(data)
print(len(data))

data_2 = data.strip()
print(data_2)
print(len(data_2))


data = "Hello"
data_2 = 'Thanks'
data_3 = 3

print(type(data))
print(data.count("ld"))

print(data.endswith('!'))
encode = data.encode()
print(type(encode))

print(encode.decode())


print(data.find('m', 8, 11))





print(data.replace('l', 'b'))
print(data.replace(['o', 'l'], ['a'], 'b'))

new_data = data.split('o')
print(new_data)
print(data + data_2 + str(data_3))

new_data = "{} {} {}".format(data, data_2, data_3)

new_data = f"{data} {data_2} {data_3}"

print(new_data)

data = "Hello \'James\' "
data = 'Hello "james" '


data = " Hello \\ james"
data = "Hello\b World"
print(data)

data = '\101\123'
print(data)

data
print(data)
print(data)





data_list = ['Apple', 'Mango','Apple', 'Mango']

data = " ".join(data_list)

print(data)

data = "Hello\tWorld\t"

print(len(data))
data_2 = data.center(20, "!")

print(len(data_2))
print(data_2)

print(data.expandtabs())


data = {
    'x': 20,
    'y': 25
}

x = 20
y = 25

new_data = '{x} {y}'.format(**data)
new_data = '{x} {y}'.format_map(data)

print(new_data)





data = "Hello, malmö! 12"
data = "THIS"
data = "23"

print(data.index('ma'))

print(data.isalnum())
print(data.isalpha())
print(data.isdigit())

s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())


s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())






function and methods



def uppercase():
    pass


class String:
    
    def uppercase():
        pass


