class Fauna:



    def __init__(self, name: str, blood_color: str):

        self.name = name

        self.blood_color = blood_color



    def eat(self):

        print(' Need food')





class Birds(Fauna):

    def __init__(self, name: str, blood_color: str, feathers: bool):

        super().__init__(name, blood_color)

        self.feathers = feathers



    def fly(self):

        print('I can fly!')





class Fishes(Fauna):

    def __init__(self, name: str, blood_color: str, gills: bool):

        super().__init__(name, blood_color)

        self.gills = gills





class Reptiles(Fauna):

    def __init__(self, name: str, blood_color: str, scales: bool):

        super().__init__(name, blood_color)

        self.scales = scales




if __name__ == '__main__':
    bird = Birds('Кеша', 'red', True)
    bird.fly()
    bird.eat()

