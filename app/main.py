class Animal:
    alive = []

    def __init__(
            self,
            name,
            health=100
    ):
        self.health = health
        self.name = name
        self.__hidden = False

        if self.health > 0:
            Animal.alive.append(self)

    def get_hidden(self):
        return self.__hidden

    def set_hidden(self, value):
        self.__hidden = value

    def __repr__(self):
        return f"{{'Name': {self.name}, 'Health': {self.health}, 'Hidden': {self.get_hidden()}}}"


class Herbivore(Animal):

    def hide(self):
        self.set_hidden(not self.get_hidden())


class Carnivore(Animal):

    def bite(
            self,
            target
    ):
        if not isinstance(target, Herbivore) or target.get_hidden():
            return

        target.health -= 50
        print(f"{self.name} bites {target.name}. {target.name}'s health is now {target.health}.")

        if target.health <= 0:
            Animal.alive.remove(target)
            print(f"{target.name} has died.")




# class Animal:
#     alive = []
#     def __init__(self, name: str, hidden=False, health: int = 100) -> None:
#         self.health = 100
#         self.name = name
#         self.hidden = hidden
#         if self.health <= 0:
#             Animal.alive.append(self)
#
# class Herbivore(Animal):
#     def hide(self) -> None:
#         if self.hidden == True:
#             self.hidden = not self.hidden
#
#
# class Carnivore(Animal):
#     def bite(self, animal: Herbivore) -> None:
#         if isinstance(animal, Herbivore) and animal.hidden == False:
#             animal.health -= 50
#             if animal.health <= 0:
#                 Animal.alive.remove(animal)
#                 print(f"{animal.name} has died.")
#         else:
#             print(f"{self.name} cannot bite {animal.name}. Either they are not a herbivore or they are hidden.")
