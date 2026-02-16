from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:

        if not isinstance(herbivore, Herbivore):
            return
        if herbivore.hidden:
            print(f"{self.name} cannot bite hidden {herbivore.name}")

        else:
            herbivore.health -= 50

        if herbivore.health <= 0 and herbivore in Animal.alive:
            Animal.alive.remove(herbivore)
