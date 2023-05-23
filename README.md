```python
my_tuple = ("fruits", "shit", True, 12)
my_tuple[0] = "pineapple"

credentials = (password, username)

print(my_tuple[0])
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))

new_list = list(my_tuple)

print(new_list)
print(type(new_list))

new_list[2] = "pineapple"
print(new_list)

my_tuple = tuple(new_list)
print(my_tuple)
print(type(my_tuple))

my_tuple[0] = 'new'
print(my_tuple)

new_tuple = ('apple',)
print(new_tuple)
print(type(new_tuple))

tuple_2 = ('banana',)

new_tuple += tuple_2
print(new_tuple)
print(dir(new_tuple))

a, *_, d = my_tuple
print(a, _, d)
```
