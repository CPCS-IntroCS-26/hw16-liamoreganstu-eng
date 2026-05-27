class Animal:
    def __init__(self, name, age, speak):
        self.name = name
        self.age = age
        self.speak = speak

    def makeSound(self):
        print(f"{self.name} says {self.speak}")

    def move(self):
        print(f'{self.name} dodged an obstacle')

    def describe(self):
        print(self.name, self.age)

    def __str__(self):
        return f"name: {self.name}\n" + \
               f"age: {self.age}\n" + \
               f"sound: {self.speak}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Woof! Woof!")
        self.breed = breed

    def makeSound(self):
        print('Woof! Woof!')

    def move(self):
        print('jumps and catches a frisbee')
    
    def describe(self):
        print(f'{self.name} is {self.age} years old and is a {self.breed}')

    def __str__(self):
        return f"names: {self.name}\n" + \
               f"age: {self.age}\n" + \
               f"sound: {self.speak}"


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age, "Flapping")
        self.can_fly = can_fly

    def move(self):
        print('flew home.')

    def describe(self):
        print(f'{self.name} is {self.age} years old and {self.can_fly} fly')

    def __str__(self):
        return f"name: {self.name}\n" + \
               f"age: {self.age}\n" + \
               f"sound: {self.speak}"


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age, "blub blub")
        self.water_type = water_type

    def move(self):
        print('swam away from the shark.')

    def makeSound(self):
        print('blub... blub')

    def describe(self):
            print(f'{self.name} is {self.age} years old and is a {self.water_type} water fish')

    def __str__(self):
        return f"name: {self.name}\n" + \
               f"age: {self.age}\n" + \
               f"sound: {self.speak}"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age, "prrrrrr")
        self.indoor = indoor

    def makeSound(self):
        print('ppprrrrr')

    def move(self):
        print('pounced on a mouse.')

    def describe(self):
        print(f'{self.name} is {self.age} years old and {self.indoor} an indoor cat')

    def __str__(self):
        return f"name: {self.name}\n" + \
               f"age: {self.age}\n" + \
               f"sound: {self.speak}"
