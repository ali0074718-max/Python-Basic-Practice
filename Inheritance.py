# Single Inheritance
class Animal:
    def eat(self):
        print("This enimal eats food.")
class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

# Multilevel Inheritance
class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

# Multiple Inheritance
class LandAnimal:
    def walk(self):
        print("Can walk on land.")
class WaterAnimal:
    def water(self):
        print("Can swim in water.")
class Frog(LandAnimal, WaterAnimal):
    def jump(self):
        print("Frog is jumping.")

my_puppy = Puppy()
my_puppy.eat()
my_puppy.bark()
my_puppy.play()

#Multiple Inheritance
frog = Frog()
frog.walk()
frog.water()
frog.jump()