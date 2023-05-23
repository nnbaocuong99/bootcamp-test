class Student:
    
    def __init__(self, number):
        self.rollno = number
    
    @staticmethod
    def show(number, number_b):
        return number + number_b
    def calculate(self):
        return self.show(self.rollno, self.rollno)

    @classmethod
    def display(cls, no):
        return cls(no)
    def _calculate(self):
        return self.rollno
    def get_rollno(self):
        return self.rollno
    def set_rollno(self, no):
        if no < 10:
            raise ValueError("Value should be greater than 10")
        self._rollno = no
    def del_rollno(self):
        del self.rollno

    rollno = property(fget=get_rollno, fset=set_rollno, fdel=del_rollno)



obj = Student(19)
print(dir(obj))
print(obj.get_rollno())
print(Student.rollno)
print(dir(obj))
print(obj.show(20, 23))
print(obj.get_rollno())
print(obj.show())
print(obj.calculate())
print(obj._calculate())
print(St.display())
print(obj.calculate())

obj2 = Student.display(30)
print(obj2.rollno)
print(obj2.calculate())
print(obj.display())



class Person:

    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone
    def person_details(self):
        return {
            "name": self.name,
            "phone": self.phone,
        }


class Student(Person):
    
    def __init__(self, name, phone, address) -> None:
        super().__init__(name, phone)
        self.address = address
    def get_address(self):
        return self.name
    def person_details(self):
        result = super().person_details()
        result['address'] = self.address
        return result

person1 = Person('James', '21312312')
print(person1.person_details())

person1 = Student('James', '21312312', 'Address Street')
print(person1.person_details())
print(person1.get_address())