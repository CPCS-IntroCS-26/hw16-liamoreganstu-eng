class Animal:
    def __init__(self, name, age, sound):
        self.__name = name
        self.__age = age
        self.__sound = sound

    def speak(self):
        print("Grrrrrrr")

    def move(self):
        pass

    def describe(self):
        pass

    def __str__(self):
        return f"name: {self.__name}\n" + \
               f"age: {self.__age}\n" + \
               f"sound: {self.__sound}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(self, name, age)
        self.__breed = breed
    
    def set_special(self, breed):
        self.__breed = breed

    def get_special(self):
        return self.__breed

    def speak(self):
        print('Woof! Woof!')

    def move(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        self.__name = name
        self.__age = age
        self.__can_fly = can_fly

    def move(self):
        pass


class Fish(Animal):
    def __init__(self, name, age, water_type):
        self.__name = name
        self.__age = age
        self.__water_type = water_type

    def move(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, indoor):
        self.__name = name
        self.__age = age
        self.__indoor = indoor

    def speak(self):
        pass

    def move(self):
        pass

dog = Dog(Animal)
dog.speak