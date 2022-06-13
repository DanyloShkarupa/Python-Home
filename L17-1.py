def animal_talk(an):
    an.talk()


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('Woof')


class Cat(Animal):
    def talk(self):
        print('Meow')


dog = Dog()
cat = Cat()
animal_talk(cat)
animal_talk(dog)