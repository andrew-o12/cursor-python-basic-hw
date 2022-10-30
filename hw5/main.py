import dataclasses
import collections
# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """


class Laptop:

    def __init__(self, name):
        self.name = name
        battery = Battery('86 Wh')
        self.laptop = [self.name, battery.battery_capacity]


class Battery:

    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


Asus = Laptop('Asus')
print(Asus.laptop)

# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation

class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self, s_type):
        self.s_type = s_type


guitar_string = GuitarString('nickel plated')
myguitar = Guitar(guitar_string.s_type)
print(myguitar.string)

# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.


class Calc:

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def add_nums(self):
        return self.a + self.b + self.c
# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_carbonara = Pasta(["tomato", "cucumber"])
print(pasta_carbonara.ingredients)
pasta_bolognaise = Pasta.bolognaise()
print(pasta_bolognaise.ingredients)

# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50

class Concert:

    max_visitor_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value if value <= Concert.max_visitor_num else Concert.max_visitor_num


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str),
#     email (str), birthday (str), age (int)
#     """


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

# 7. Create the same class (6) but using NamedTuple


AddressBook = collections.namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email',
                                                     'birthday', 'age'])
# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='',
#     email='', birthday= '', age='')


class AddressBook2:
    def __init__(self, key: int, name: str, phone_number: str, address: str, email: str, birthday: str, age: int):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return f'AddressBook(key= {self.key}, name= {self.name}, phone_number= {self.phone_number},' \
               f'address= {self.address}, email= {self.email}, birthday= {self.birthday}, age= {self.age})'


print(AddressBook2(1, 'myname', '222 2222', 'mycity', 'myemail@test.com', '01.01.0001', 11))

# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"


class Person:

    name = "John"
    age = 36
    country = "USA"


Person.age = 35
print(Person.age)

# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


class Student:

    id = 0
    name = ""

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.student_email = email


my_student = Student(11, 'myname', 'myemail@test.com')
print(getattr(my_student, 'student_email'))
