class Animal:
    def __init__(self, name, age, speak):
        self.__name = name
        self.__age = age
        self.__speak = speak

    def speak(self):
        print(f"{self.__name} says {self.__speak}")

    def move(self):
        print(f'{self.__name} dodged an obstacle')

    def describe(self):
        pass

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
        print('jumps and catches a frisbee.')


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(self, name, age)
        self.can_fly = can_fly

    def move(self):
        pass


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(self, name, age)
        self.water_type = water_type

    def move(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(self, name, age)
        self.indoor = indoor

    def speak(self):
        pass

    def move(self):
        pass
