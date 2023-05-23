data = {
    "a": 12,
    "b": 34
}

print(type(data))

from typing import NamedTuple
class MyDict(NamedTuple):
    a: int
    b: str

obj = MyDict(12, 'something')

printtype(obj)
print(obj)
print(obj.a)
print(obj.b)

# obj1 = data from table 1
# obj2 = data from table 2

def process_data(object_of_class_student):
    print(object_of_class_student.rollno)
    print(object_of_class_student.firstname)
    print(object_of_class_student.email)
class Student(NamedTuple):
    rollno: int 
    firstname: str
    email: str


student_obj = Student('23a', 'jahan', 'aaaa')
process_data(student_obj)
print(student_obj)
print(type(student_obj.rollno))

def my_func():
    pass

print(my_func())

def calculate_number(a: int = 5, b: int = None) -> str:
    """
    details of this function
    :param a: interger datatype
    """
    result = a + b 
    return result

Usecase (requirements),

def test_calculate_numbers():
    a = 23
    b = 34
    result = calculate_number(a=10, b=20)
    print(result)
    print(type(result))

    if result == 57:
        print('correct result')
    else:
        print('wrong')

test_calculate_numbers()
print( '20' + 20)

def my_func(a=None, *args, **kwargs):
    print('Values are: ', kwargs)
    print('Values are: ', args)
    print('Values are: ', a)

data = {
    "name": "Jaahn",
    "rollno": 20
}

my_function(2022, data=data)

def my_func(a, b):
    if a:
        pass
    if b: pass

lambda argument: expressipon

result = lambda a, b: a * b

print(type(result))
print(result(10, 2))

def check(n):
    return lambda a: a * n

result = check(n=2)
print(result(a=10))