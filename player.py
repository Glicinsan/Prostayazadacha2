class Character:
    def __init__(self, name, health, mana):
        '''
        :param name: имя
        :param health: количество жизней у персонажа
        :param mana: количество маны у персонажа
        '''

        self.name = name
        self.health = health
        self.mana = mana

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health}, Мана: {self.mana})"

# Класс для игрока
class Player(Character):
    def __init__(self, name, health, mana, weapon, ability_damage, ability_cost):
        '''
        :param name: имя игрока
        :param health: здоровья
        :param mana: очки маны
        :param weapon: название оружия
        :param ability_damage: урон специальной атаки
        :param ability_cost: сколько специальная атака требует маны
        '''
        super().__init__(name, health, mana)
        self.ability_damage = ability_damage
        self.ability_cost = ability_cost
        self.weapon = weapon

    def attack(self, target):
        damage = self.weapon.damage
        target.health -= damage
        print(f"{self.name} атакует {target.name} с помощью {self.weapon.name} и наносит {damage} урона!")

    def use_ability(self, target):
        if self.mana >= self.ability_cost:
            self.mana -= self.ability_cost
            damage = self.ability_damage
            target.health -= damage
            print(f"{self.name} использует специальную атаку и наносит {self.ability_damage} урона!")
        else:
            print(f"У {self.name} недостаточно маны")

# Класс для противников
class Enemy(Character):
    def __init__(self, name, health, mana, damage, ability_damage, ability_cost):
        '''
        :param name: имя противника
        :param health: очки здоровья
        :param mana: кол-во маны
        :param damage: сколько урона наносит
        :param ability_damage: урон специальной атаки
        :param ability_cost: сколько маны требуется для использования специальной атаки
        '''
        super().__init__(name, health, mana)
        self.damage = damage
        self.ability_damage = ability_damage
        self.ability_cost = ability_cost

    def attack(self, target):
        damage = self.damage
        target.health -= damage
        print(f"{self.name} атакует {target.name} и наносит {damage} урона!")

    def use_ability(self, target):
        if self.mana >= self.ability_cost:
            self.mana -= self.ability_cost
            damage = self.ability_damage
            target.health -= damage
            print(f"{self.name} использует способность и наносит {damage} урона!")
        else:
            print(f"У {self.name} недостаточно маны")