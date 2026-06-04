#

# ! Data Structure
# -----------------------------------------------------------------|
#   Structure  | Changeable  |  Ordered  | Repeated  | Add-Remove  |
# -------------|-------------|-----------|-----------|------------ |
#   List []    |     Yes     |    Yes    |    Yes    |    Yes      |
# -------------|-------------|-----------|-----------|-------------|
#   Set {}     |     Yes     |    No     |    No     |    Yes      |
# -------------|-------------|-----------|-----------|------------ |
#   Tuple ()   |     No      |    Yes    |    Yes    |    No       |
# -------------|-------------|-----------|-----------|------------ |
# Dictionary {}|     Yes     |    Yes    |    Yes    |    Yes      |
# -------------|-------------|-----------|-----------|-------------|


# %%
# ! Lists
fruits = ["Apple", "Banana", "Cherry", "Orange"]
len(fruits)  # 4
print("Number of fruids: ", len(fruits))

# ? Adding a new variable end of the list
fruits.append("Watermelon")
print(fruits)

# ? Add a new item to the beginning of the list
fruits.insert(0, "Pineapple")
print(fruits)

# ? Updating
fruits[1] = "Mango"
print(fruits)

# ? Removing a variable
fruits.pop()
print(fruits)

# ? Removing a variable with index number
fruits.pop(3)
print(fruits)

# ? Choose a variable
fruits[1]  # Mango
fruits[-1]  # Orange
fruits[0:2]  # ['Pineapple', 'Mango']


# %%
# ! Tuples

database = ("localhost", "admin", 12345)

database.count("admin")  # 1
print("Index of the admin in the database", database.index("admin"))
# Index of the admin in the database 1


# %%
# ! Set
set1 = {1, 2, 3}
print(set1)  # {1, 2, 3}

set11 = {1, 2, 3, 4, 5, 5, 5, 5, 5}
print(set11)  # {1, 2, 3, 4, 5}

set2 = {3, 4}

print(set2.difference(set1))  # {4}
print(set1.difference(set2))  # {1, 2}

print(set2.intersection(set1))  # {3}
print(set1.intersection(set2))  # {3}

# %%
# ! Dictionary
person = {"Name": "John", "Surname": "DOE", "Age": 40}
print("Person: ", person)
# Person: {"Name": "John", "Surname": "DOE", "Age": 40}


persons = {
    "name": ["John", "Jim", "Jane", "Julia", "Jenny"],
    "city": ["New York", "Boston", "Chicago", "San Francisco", "Washington DC"],
}

print("Persons: ", persons)

# ? Adding a new column to dictionary
persons["age"] = [20, 33, 45, 67, 8]
print("Persons: ", persons)

# %%
# ! Functions


# w/o parameters
def hello():
    print("Hello function running: \nHello World!")


hello()


# W parameters
def hello_name(name="Guess"):
    print(f"Hello_name function running:\n Hello {name}")


hello_name("Jack")
hello_name()


def calculate_salary(salary, tax_ratio):
    print(
        "Calculate_salary function running: \nSalary after tax: ",
        salary * (1 - tax_ratio),
    )


calculate_salary(100, 0.25)


# if You don't use print or similar function, response of the code can not show in the screen
def calculate_salary2(salary, tax_ratio):
    return "Calculate_salary2 function running: Salary after tax: ", salary * (
        1 - tax_ratio
    )


calculate_salary2(100, 0.25)

# %%
# ! Object Oriented Programming


class Cars:
    pass


car1 = Cars()


class Bus:
    passengers = []


NewYork_bus = Bus()
NewYork_bus.passengers.append("Jack")
NewYork_bus.passengers.append("Jim")
NewYork_bus.passengers.append("Jenny")
NewYork_bus.passengers.append("John")

print("Passenger list of New York bus: ", NewYork_bus.passengers)
# Passenger list of New York bus:  ['Jack', 'Jim', 'Jenny', 'John']

Miami_bus = Bus()
print("Passenger list of Miami bus: ", Miami_bus.passengers)
# Passenger list of Miami bus:  ['Jack', 'Jim', 'Jenny', 'John']


class Bus2:
    def __init__(self):
        self.passengers = []


NewYork_bus2 = Bus2()
NewYork_bus2.passengers.append("Jack")
NewYork_bus2.passengers.append("Jim")
NewYork_bus2.passengers.append("Jenny")
NewYork_bus2.passengers.append("John")

print("Passenger list of the second New York bus: ", NewYork_bus2.passengers)
# Passenger list of the second New York bus:  ['Jack', 'Jim', 'Jenny', 'John']

Miami_bus2 = Bus2()
print("Passenger list of the second Miami bus: ", Miami_bus2.passengers)
# Passenger list of the second Miami bus:  ['Jack', 'Jim', 'Jenny', 'John']


class Car:
    wheels = 4
    passengers = []

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print("Car created")


car1 = Car("BMW", "M5", 2020)
car2 = Car("Mercedes", "GLX", 2020)

print("First car's brand: ", car1.brand)
print("Second car's brand: ", car2.brand)


class Cars:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = "stopped"
        self.velocity = 0

    def drive(self):
        print("Engine is running")
        self.engine = "Engine is running"

    def stop(self):
        print("Engine is stopped")
        self.engine = "stopped"

    def accelerate(self, acceleration):
        self.velocity = self.velocity + acceleration


car3 = Cars("BMW", "M5", 2023, "")
print("Position of the car's engine: ", car3.engine)

car3.drive()
print("Velocity of the car's engine: ", car3.velocity)

car3.accelerate(50)
print("Velocity of the car's engine: ", car3.velocity)


# %%
# ! Encapsulation
class BankAccount:
    def __init__(self, name, iban):
        self.name = name
        self.iban = iban
        self.amount = 0


bank_account = BankAccount("John", "TR90000012341234")

print("Amount of bank account: ", bank_account.amount)  # Amount of bank account:  0

bank_account.amount = 1000
print("Amount of bank account: ", bank_account.amount)  # Amount of bank account:  1000

# -----------------------------------------------------------------|
#  Usage Instruction  |    Name     |           Meaning            |
# --------------------|-------------|------------------------------|
#       Name          |   Public    |    Everyone accessible       |
# --------------------|-------------|------------------------------|
#       _Name         |  Protected  |  Touching is not recommended |
# --------------------|-------------|------------------------------|
#      __Name         |  Private    |    Access is restricted      |
# --------------------|-------------|------------------------------|
#       _Name         |  Protected  |Python-specific system command|
# --------------------|-------------|------------------------------|


class BankAccount2:
    def __init__(self, name, iban):
        self.name = name
        self.iban = iban
        self.__amount = 0

    def show_amount(self):  # getter function
        print("Amount of bank account: ", self.__amount)

    def add_amount(self, amount):  # setter function
        self.__amount = self.__amount + amount


bank_account = BankAccount2("John", "TR90000012341234")

# print(
#     "Amount of bank account: ", bank_account.amount
# )  # You can not reach bank account amount

bank_account.show_amount()  # Amount of bank account:  0

bank_account.add_amount(1000)
bank_account.show_amount()  # Amount of bank account:  1000


# %%
# ! Inheritance
class Animal:
    def __init__(self, name):
        self.name = name


class Dog:
    print("Wof wof")


dog1 = Dog()


# print("Name of dog1: ", dog1.name)  # dog1 does not have name


class Dog2(Animal):
    print("Wof wof")


dog2 = Dog2("Charles")
print("Name of dof2: ", dog2.name)


class Cat:
    print("Meow meow")
