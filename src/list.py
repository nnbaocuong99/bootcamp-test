my_list = ["apple", "mango", 'cherry', 'cherry']
new_list = []
my_list_2 = [0, 1, 2]

print(my_list)
print(len(my_list))
print(type(my_list))
print(my_list[1:])

if "apple" in my_list:
    print("Exists")

my_list.append("grapes")
my_list[:1] = ["banana"]
my_list.remove("cherry")
my_list.insert(1, "banana")
my_list.extend(my_list_2)
my_list.pop(1)

del my_list
my_list.clear()

print(my_list)

for x in my_list:
    print(x)
for x in range(len(my_list)):
    print(my_list[x])

my_list = ["apple", "mango", 'cherry', 'cherry']
fruits = []
for fruit in my_list:
    if fruit != "apple":
        # print(fruit)
        fruits.append(fruit)

fruits = [ fruit for fruit in my_list if fruit != "apple" ]
print(fruits)

my_list.sort(reverse=True)
my_list.reverse()

new_list = my_list.copy()
new_list = my_list

new_list.pop()
my_list.pop(1)

print(new_list)
print(my_list)

my_list.append('NEW ONE')

print(new_list)
print(my_list)
print(my_list.count('cherry'))
print(my_list.index('cherry'))