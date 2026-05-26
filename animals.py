class Animal:
    def __init__(self, name, age, speak):
        self.__name = name
        self.__age = age
        self.__speak = speak

    def speak(self):
        print(f"{self.name} says {self.speak}")

    def move(self):
        print(f'{self.__name} dodged an obstacle')

    def describe(self):
        print(self.__name, self.__age)

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__speak}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(self, name, age)
        self.breed = breed

    def speak(self):
        print('Woof! Woof!')

    def move(self):
        print('jumps and catches a frisbee')
    
    def describe(self):
        print(f'{self.name} is {self.__age} years old and is a {self.breed}')

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__speak}"


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(self, name, age)
        self.can_fly = can_fly

    def move(self):
        print('flew home.')

    def describe(self):
        print(f'{self.name} is {self.__age} years old and {self.can_fly} fly')

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__speak}"


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(self, name, age)
        self.water_type = water_type

    def move(self):
        print('swam away from the shark.')

    def speak(self):
        print('blub... blub')

    def describe(self):
            print(f'{self.name} is {self.__age} years old and is a {self.water_type} water fish')

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__speak}"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(self, name, age)
        self.indoor = indoor

    def speak(self):
        print('ppprrrrr')

    def move(self):
        print('pounced on a mouse.')

    def describe(self):
        print(f'{self.name} is {self.__age} years old and {self.indoor} an indoor cat')

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__speak}"
