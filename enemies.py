import items
from random import randint

class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Spartos(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__(name="Spartos", hp=10, damage=2)
        elif level == 2:
            super().__init__(name="Spartos", hp=15, damage=4)
        elif level == 3:
            super().__init__(name="Spartos", hp=20, damage=6)
        elif level == 4:
            super().__init__(name="Spartos", hp=25, damage=10)
        elif level == 5:
            super().__init__(name="Spartos", hp=30, damage=15)
        else:
            if isinstance(level, int):
                raise ValueError("Enemy level must be between 1 and 5.")
            else:
                raise TypeError("Enemy level must be an integer.")

        self.inventory = []
        self.inventory.append(items.Coin(randint(level, level*2)))

class Harpy(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__(name="Spartos", hp=15, damage=4)
        elif level == 2:
            super().__init__(name="Spartos", hp=20, damage=8)
        elif level == 3:
            super().__init__(name="Spartos", hp=25, damage=12)
        elif level == 4:
            super().__init__(name="Spartos", hp=30, damage=15)
        elif level == 5:
            super().__init__(name="Spartos", hp=50, damage=20)
        else:
            if isinstance(level, int):
                raise ValueError("Enemy level must be between 1 and 5.")
            else:
                raise TypeError("Enemy level must be an integer.")

        self.inventory = []
        self.inventory.append(items.Coin(randint(level, level*2)))
        for i in range(randint(level-1, level+2)):
            self.inventory.append(items.Feather())
        if randint(1,100) < level*20: self.inventory.append(items.Claw())
