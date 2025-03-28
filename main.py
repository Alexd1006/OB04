from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self,weapon):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец выбирает меч.\nБоец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец выбирает лук.\nБоец стреляет из лука."

class Crossbow(Weapon):
    def attack(self):
        return "Боец выбирает арбалет.\nБоец стреляет из арбалета."

class Fighter():
    def __init__(self,name,weapon: Weapon):
        self.name = name
        self.weapon = weapon
    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
    def attack(self):
        return self.weapon.attack()


class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage=100):
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return f"Монстр получил урон, осталось {self.health} здоровья."

fighter = Fighter("Герой", Sword())
monster = Monster(150)



print(fighter.attack())
print(monster.take_damage())

fighter.change_weapon(Crossbow())
print(fighter.attack())
print(monster.take_damage())