from animals import Animal, Dog, Bird, Fish, Cat


def main():
    # Create one instance of each animal subclass
    my_dog = Dog('george', 8, 'pug')
    my_bird = Bird('flappy', 2, 'can')
    my_fish = Fish('sushi', 1, "salt")
    my_cat = Cat('sally', 5, 'is')

    animals = [my_dog, my_bird, my_fish, my_cat]

    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        animal.makeSound()
        animal.move()
        animal.describe()


if __name__ == "__main__":
    main()
