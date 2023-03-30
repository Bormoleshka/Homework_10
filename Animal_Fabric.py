from fauna import Fishes, Reptiles, Birds

class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"bird": Birds, "fish": Fishes, "reptile": Reptiles}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("bird", "red", "feathers")
    animal_from_fabric.characteristic = ["летает", "поет"]
    print(animal_from_fabric)
