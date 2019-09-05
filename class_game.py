class Game:
    def __init__(self, name="No name", x=0, y=0, hp=100, damage=10, speed=2):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.speed = speed

        print(f"New hero: {self.name}")
        print(f"Coordinates: {self.x, self.y}")
        print(f"Health points: {self.hp}")
        print(f"Damage: {self.damage}")
        print(f"Speed: {self.speed}")
        print("\n")


    def run(self, direct):
        if self.hp > 0:
            self.x += self.speed*direct
            print(f"{self.name} переместился на {self.x, self.y} \n")
        else:
            print(f"{self.name} мёртв \n")

    def shoot(self, target):
        if ((self.x - target.x)**2 + (self.y - target.y)**2) > 10:
            print("Невозможно выстрелить (слишком большое расстояние между игроками) \n")
        else:
            self.hp -= 10
            print(f"{self.name} нанес {target.name} 10 урона \n")
            print(f"{target.name} теперь имеет {self.hp} hp \n")

class Performance(Game):
    def fly(self, x=10, y=20):
        if self.hp > 0:
            self.x += x
            self.y += y
            print(f"{self.name} полетел на {self.x, self.y} \n")
        else:
            print(f"{self.name} мертв \n")

    def took_boost(self):
        if self.hp > 0:
            self.x += 100
            print(f"{self.name} подобрал буст и со скоростью +100 переместился на {self.x, self.y} \n")
        else:
            print(f"{self.name} мертв \n")

    def slow(self):
        if self.hp > 0:
            self.x += 0.2
            print(f"{self.name} подобрал замедление и передвинулся на расстояние 0.2 на {self.x, self.y} \n")
        else:
            print(f"{self.name} мертв \n")


character_1 = Performance("Карл")
character_2 = Performance("Боб")

character_1.run(1)
character_1.run(1)
character_2.run(1)

character_1.shoot(character_2)
character_1.shoot(character_2)
character_1.shoot(character_2)

character_2.shoot(character_1)
character_2.shoot(character_1)

character_1.fly()



character_1.took_boost()

character_1.slow()
character_1.took_boost()

character_1.shoot(character_2)

character_2.slow()

character_1.took_boost()

character_1.shoot(character_2)

