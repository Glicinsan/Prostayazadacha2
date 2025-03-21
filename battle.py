import random
from player import *
class Weapon:
    def __init__(self, name, damage):
        '''
        :param name: название оружия
        :param damage: урон
        '''
        self.name = name
        self.damage = damage


# Класс для управления сражениями
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"{self.player.name}, ваш противник {self.enemy.name}!")
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"\n{self.player}")
            print(f"{self.enemy}")
            print("1. Атаковать")
            print("2. Использовать способность")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.player.attack(self.enemy)
            elif choice == "2":
                self.player.use_ability(self.enemy)
            else:
                print("Неверный выбор, пропускаем ход.")

            if self.enemy.is_alive():
                if random.choice([True, False]):  # Рандомно выбирается тип атаки противника
                    self.enemy.attack(self.player)
                else:
                    self.enemy.use_ability(self.player)

        if self.player.is_alive():
            print(f"\n{self.player.name} побеждает {self.enemy.name}!")
        else:
            print(f"\n{self.player.name} был побежден {self.enemy.name}!")

# Класс для общей логики игры
class Game:
    def __init__(self):
        self.player = None
        self.enemies = []

    def setup(self):
        print("Добро пожаловать в игру!")
        player_name = input("Введите имя вашего персонажа: ")
        weapon_choice = self.choose_weapon()
        self.player = Player(player_name, 100, 50, weapon_choice, 30, 15)
        self.enemies = [
            Enemy("Гоблин", 100, 20, 10, 15, 10),
            Enemy("Орк", 130, 30, 15, 20, 15)
        ]

    def choose_weapon(self):
        weapons = [
            Weapon("Меч", 70),
            Weapon("Лук", 65)
        ]
        print("\nВыберите оружие:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon.name} (Урон: {weapon.damage}")
        choice = int(input("Ваш выбор: ")) - 1
        return weapons[choice]

    def start(self):
        self.setup()
        for enemy in self.enemies:
            battle = Battle(self.player, enemy)
            battle.start()
            if not self.player.is_alive():
                break
        if self.player.is_alive():
            print("\nПоздравляем! Вы победили всех противников!")
        else:
            print("\nИгра окончена. Вы проиграли.")
