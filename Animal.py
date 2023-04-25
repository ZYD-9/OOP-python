class Animal:
    age = 0
    gender = " "
    def __init__(self,name,animal_family):
        self.name = name
        self.animal_family = animal_family


    def is_Mammal(self):
        if self.animal_family == 1:
            print(f'{self.name} is mammal')
            return True
        else:
            print(f'{self.name} is not a mammal')
            return False

    def mate(self):
        if self.gender.upper() == 'MALE':
            print(f"{self.name} is mated to female")
        elif self.gender.upper() == 'FEMALE':
            print(f'{self.name} is mated to male')
        else:
            print(f'Please provide a valid gender to {self.name}')


#animal = Animal("mojo",1)
#animal.gender = 'female'
#animal.is_Mammal()
#animal.mate()

class Duck(Animal):
    beak_color = 'Yellow'

    def __init__(self,name,animal_family):
        super().__init__(name,animal_family)

    def swim(self):
        print(f'{self.name} is a duck that swims')
    def quack(self):
        print(f'{self.name} : Quack!,Quack!')

duck1 = Duck('Donald',2)
duck1.swim()

class Fish(Animal):
    sizeinFt = 4
    canEat = True

    def __init__(self,name,animal_family):
        super().__init__(name, animal_family)

    def __swim(self):
        print(f'{self.name} is swimming under the sea')

class Zebra(Animal):

    is_wild = True

    def __init__(self,name,animal_family):
        super().__init__(name,animal_family)

    def run(self):
        print(f'{self.name} is running')

zebra1 = Zebra('Maurice',2)
zebra1.is_Mammal()









