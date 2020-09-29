import items
import enemies

class MapTile:
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a strange room.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass


class EmptyTile(MapTile):
    def intro_text(self):
        return """
        There's nothing to see here.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass


class LootTile(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyTile(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining."\
            .format(self.enemy.damage, the_player.hp))


class StoneTile(LootTile):
    def __init__(self, x, y):
        super().__init__(x, y, items.Stone())

    def intro_text(self):
        return """
        You found a stone. Maybe you can use it as a weapon.
        """


class SpartoiTile(EnemyTile):
    def __init__(self, x, y, level):
        super().__init__(x, y, enemies.Spartos(level))

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            One of the mythical Spartoi rises from the ground and attacks you!
            """
        else:
            return """
            The skeleton of a defeted Spartos lies crumpled at your feet.
            """


class HarpyTile(EnemyTile):
    def __init__(self, x, y, level):
        super().__init__(x, y, enemies.Harpy(level))

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A harpy sweeps down from the ceiling and attacks you!
            """
        else:
            return """
            The rotting corpse of a harpy lies at your feet.
            """
