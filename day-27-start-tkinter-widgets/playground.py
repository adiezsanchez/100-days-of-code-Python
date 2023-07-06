# Creating a function with unlimited positional arguments that sums them all together
# This creates a tuple containing all the arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add (1,2,3,4))

# You can also access particular positions in the *args tuple by typing its index

def show_args_at_index_0(*args):
    print(args[0])

show_args_at_index_0(22, 1, 2 ,3)

# Creating a function with unlimited keyword arguments
# This creates a dictionary containing the arguments as a key:value pair

def calculate_test(**kwargs):
    print(kwargs)
    # You can also loop through the **kwargs as dictionaries
    for key, value in kwargs.items():
        print(key)
        print(value)
    #Yoy can also access the values associated with each key
    print(kwargs["add"])

calculate_test(add=3, multiply=5)

# Use it as a calculate function, the problem with this syntax is that if you do not declare
# all the defined kwargs key:value pairs as input parameters it will raise and error.
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(5, add=3, multiply=5)

# Creating a class with **kwargs:

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        # self.color = kwargs["color"] This line would rise a KeyError: 'color' error as we are
        # not inputting any color kwargs.
my_car = Car(make="Ford", model="Mustang")

print (my_car.make)
print (my_car.model)

# An alternative to avoid raising errors is using the kwargs.get() function instead of the
# kwargs[key] syntax, that if it remains unused, it will return None.

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
my_car = Car(make="Ford", model="Mustang")

print (my_car.make)
print (my_car.model)
print (my_car.color)
print (my_car.seats)