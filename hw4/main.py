# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed,
# break_speed, mileage_info

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self, increase):
        print(f'Speed has been increased to {increase} km/h')

    def break_speed(self, reduce):
        print(f'Speed has been reduced to {reduce} km/h')

    def mileage_info(self):
        print(f'Mileage is {self.mileage} km')


myvechicle = Vehicle(100, 11111)
myvechicle.increase_speed(150)
myvechicle.break_speed(15)
myvechicle.mileage_info()


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод
# seating_capacity

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity):
        print(f'The seat capacity of the bus is {capacity} passengers')


mybus = Bus(60, 22222)
mybus.seating_capacity(65)

# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)

print(issubclass(Bus, Vehicle))

# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus

school_bus = Bus(60, 22222)
print(f'Is school_bus Vehicle class object? {isinstance(school_bus, Vehicle)}')
print(f'Is school_bus Bus class object? {isinstance(school_bus, Bus)}')


# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address,
# main_subject

class School:
    def __init__(self, school_id, number_of_students):
        self.get_school_id = school_id
        self.number_of_students = number_of_students

    def school_address(self, school_address):
        print(f'The school address is {school_address}')

    def main_subject(self, main_subject):
        print(f'The main subject is {main_subject}')


myschool = School(1, 300)
myschool.school_address('Unknown')
myschool.main_subject('Undefined')


# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
class SchoolBus(School, Bus):
    def bus_school_color(self, bus_school_color):
        print(f'The bus school color is {bus_school_color}')


mybus = SchoolBus((65, 22222), (1, 300))
mybus.bus_school_color('yellow')


# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри:
# від Ведмідь і від Вовк,
# створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.

class Animal:
    def __init__(self):
        self.name = 'animal'
        self.meal = 'meal'

    def eat(self):
        print(f'{self.name} eats {self.meal}')


class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Bear'
        self.meal = 'Fish'


class Wolf(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Wolf'
        self.meal = 'Meat'


bear = Bear()
wolf = Wolf()
animal = (bear, wolf)

for e in animal:
    e.eat()


# Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу,
# лише коли population > 1500,інакше повертається повідомлення: "Your city is too small".
# Підказка: використовуєте для цього завдання магічні методи

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population
        print(f"Your city population > 1500 {self.name}")


Kyiv = City('Kyiv', 3500)
Vinnitsa = City('Vinnitsa', 1400)