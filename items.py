class Item():
    """The base class for all items in the game."""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n{}\n{}\nValue: {}\n".format(self.name, self.hr,
                                    self.description, self.value)

    @property
    def hr(self, rule=""):
        for i in range(len(self.name)+8): rule += "="
        return rule


class Coin(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Coin", description="A strange coin with Zeus' " \
                        "face stamped on top. A mark on the back shows that" \
                        " it is worth {} Drachma.".format(str(self.amount)),
                        value=self.amount)


#Weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage, weight, max_uses):
        self.damage = damage
        self.weight = weight
        self.max_uses = max_uses
        self.uses = 0
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n{}\n{}\n\nValue: {}\nDamage: {}\nWeight: {}\nUses Left: {}"\
                .format(self.name, self.hr, self.description, self.value,
                self.damage, self.weight, self.remaining_uses)

    @property
    def hr(self, rule=""):
        for i in range(len(self.name)+8): rule += "="
        return rule

    @property
    def remaining_uses(self):
        return self.max_uses - self.uses


class Stone(Weapon):
    def __init__(self):
        super().__init__(name="Stone", description="A piece of stone from the" \
                        " tower wall. It might work as a weapon in a pinch.",
                        value=0, damage=2, weight=2, max_uses=1)


class Claw(Weapon):
    def __init__(self):
        super().__init__(name="Harpy's Claw", description="A claw from a " \
                        "slain harpy. It should work as a weapon.",
                        value=0, damage=5, weight=2, max_uses=5)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword", description="A short sword, known as a" \
                        "Xiphos. You don't really know how to use it, but " \
                        "it's better than nothing", value=10, damage=10,
                        weight=10, max_uses=15)


class Spear(Weapon):
    def __init__(self):
        super().__init__(name="Spear", description="A spear, called a Doru. " \
                        "The familar weapon of the heroes. It will serve you" \
                        " well.", value=20, damage=15, weight=15, max_uses=25)


#Enemy Drops
class Feather(Item):
    def __init__(self):
        self.weight = 1
        super().__init__(name="Feather", description="A feather.", value=1)
