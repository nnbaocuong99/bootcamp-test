my_set = {"apple", "mango"}
my_set = {"apple", "mango", "mango1", True, 12}

print(my_set)
print(len(my_set))
print(type(my_set))
print("apple" in my_set)

my_set.add('23')

print(my_set)

my_set2 = ['pineapple', 'pineapple']
my_set.update(my_set2)
check = my_set.remove("pineapple")
my_set.discard("pineapple2")
check = my_set.pop()
check = my_set.clear()

del my_set

print(my_set)
print(check)

my_list = ["apple", "mango", "mango"]
print(my_list)
my_set2 = set(my_list)
print(my_set2)

my_set = {"apple", "mango"}
my_set2 = {"apple", "banana", "pineapple"}
my_set3 = { "cherry"}

my_set.intersection_update(my_set2)

new_data = my_set.intersection(my_set2)
my_set.symmetric_difference_update(my_set2)
my_set.symmetric_difference_update(my_set2)
new_data = my_set.symmetric_difference(my_set2)

new_data = my_set.union(my_set2, my_set3)
print(my_set)
print(new_data)