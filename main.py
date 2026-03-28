import random
import time


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def take_damage(self, taken_damage):
        self.hp -= taken_damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} отримав {taken_damage} шкоди. Залишилось {self.hp} життя!")

    def attack(self, target):
        print(f"{self.name} атакував {target.name}...")
        target.take_damage(self.damage)

    def drop_item(self):
        chance = random.randint(0,100)
        item_counter = 0
        if chance  < 5:
            item_counter = 3
        elif chance < 25:
            item_counter = 2
        elif chance < 50:
            item_counter = 1


        if item_counter > 0:

            print(f"Ви знайшли {item_counter} предметів!")
            for i in range(item_counter):
                class_item = random.randint(0,1)
                if class_item == 0:
                    dropped_item = random.choice(weapon_items)
                else:
                    dropped_item = random.choice(weapon_items)
                print(f"Ваша здобич: {dropped_item.name}"
                      f"\t Бонусна шкода:{dropped_item.bonus_damage}\n"
                      f"\t Бонусна броня:{dropped_item.bonus_armor}\n"
                      f"\t Бонусне ХП:{dropped_item.bonus_hp}\n"
                      f"\t Екіпіювати(1) чи викинути(будь яка кнопка)?\n")
                user_answer = input("Зробіть вибір(1 чи 2):")
                if user_answer == 1:
                    my_hero.equip_weapon(dropped_item) if class_item == 0 else my_hero.equip_armor(dropped_item)
                else:
                    print(f"Ви викинули {dropped_item.name}")

        else:
            print("На жаль, вам нічого не випало! Удачи в боях")

class Player:
    def __init__(self, name, player_class, maxhp, damage):
        self.name = name
        self.player_class = player_class
        self.bonus_armor = 0
        self.weapon = None
        self.accessorie = None
        self.armor = None
        self.maxhp = maxhp
        self.hp = maxhp
        self.damage = damage

    def take_damage(self, taken_damage):
        actual_damage = taken_damage - self.bonus_armor
        if actual_damage < 1:
            actual_damage = 1
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} отримав {actual_damage} шкоди (захист поглинув {self.bonus_armor}). Залишилось {self.hp} життя!")

    def take_damage(self, taken_damage):
        self.hp -= taken_damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} отримав {taken_damage} шкоди. Залишилось {self.hp} життя!")

    def attack(self, target):
        print(f"{self.name} атакував {target.name}...")
        target.take_damage(self.damage)

    def player_info(self):
        print(f"-----{self.name}-----"
              f"Клас:{self.player_class}\n"
              f"Життя:{self.hp}\n"
              f"Шкода:{self.damage}\n")

    def equip_weapon(self, item):
        if item.item_class != self.player_class:
            print(f"Упс, Я не можу використовувати {item.name}")
            return
        self.armor = item
        self.hp += item.bonus_hp
        self.armor += item.bonus_armor
        print(f"Ви це взяли {item.name}, Ваша шкода збільшена на {item.bonus_damage}")

    def equip_armor(self, item):
        if item.item_class != self.player_class:
            print(f"Упс, я не можу одягнути {item.name}")
            return
        self.armor = item
        self.maxhp += item.bonus_hp
        self.bonus_armor += item.bonus_armor
        print(f"Ви одягли {item.name}! Життя +{item.bonus_hp}, Броня +{item.bonus_armor}")

    def healing(self, procent):
        heal = (self.max_hp/100) * procent
        if self.hp + heal > self.max_hp:
            self.hp = self.max_hp
            print(f"Ви повністю поповнили ХП")
        else:
            self.hp += heal
            print(f"Ви відновили {heal} ХП! тепер у вас {self.hp} з {self.max_hp}")

    def equip_accessorie(self, item):
        self.armor = item.bonus_armor
        self.maxhp = item.bonus_hp
        self.damage = item.bonus_damage
        self.accessorie = item

class Item:
    def __init__(self, name, item_class, bonus_damage, bonus_hp, bonus_armor):
        self.name = name
        self.item_class = item_class
        self.bonus_damage = bonus_damage
        self.bonus_hp = bonus_hp
        self.bonus_armor = bonus_armor

    def equip_armor(self, item):
        pass


class Item:
    def __init__(self, name, item_class, bonus_damage, bonus_hp, bonus_armor):
        self.name = name
        self.item_class = item_class
        self.bonus_damage = bonus_damage
        self.bonus_hp = bonus_hp
        self.bonus_armor = bonus_armor


list_of_enemy = [
        # Рядові вороги (Слабкі)
        Enemy("Слизовик", 20, 3), Enemy("Кажан", 15, 5), Enemy("Щур", 25, 4), Enemy("Скелет-новобранець", 40, 6),
        Enemy("Гоблін", 35, 7), Enemy("Павук", 30, 5), Enemy("Зомбі", 50, 4), Enemy("Дикий пес", 25, 8),
        Enemy("Тінь", 20, 10), Enemy("Кобольд", 40, 6), Enemy("Заражена рослина", 45, 5), Enemy("Гнилий труп", 55, 3),
        Enemy("Малий біс", 30, 9), Enemy("Крадій", 40, 8), Enemy("Кам'яний жук", 60, 4), Enemy("Лісовий дух", 35, 7),
        Enemy("Вогонь-блукач", 25, 12), Enemy("Зміїний воїн", 45, 9), Enemy("Гарпія-молодик", 35, 10),
        Enemy("Орк-слуга", 55, 8),
        Enemy("Культист", 40, 11), Enemy("Живий обладунок (іржавий)", 70, 5), Enemy("Мімік (малий)", 50, 10),
        Enemy("Крижаний уламок", 30, 11),
        Enemy("Гієна", 30, 9), Enemy("Бандит", 45, 10), Enemy("Скелет-лучник", 35, 12), Enemy("Темний пацюк", 20, 15),
        Enemy("Морський гад", 50, 8), Enemy("Загублена душа", 15, 18), Enemy("Варан", 65, 7), Enemy("Гниле дерево", 80, 4),
        Enemy("Гриб-паразит", 40, 6), Enemy("Мандрівний вогник", 20, 14), Enemy("Старий вовк", 50, 11),
        Enemy("Здичавілий кріп", 45, 9),
        Enemy("Падлоїд", 55, 7), Enemy("Болотна жаба", 40, 8), Enemy("Тюремник", 60, 10), Enemy("Найманець", 50, 12),

        # Елітні вороги (Середні)
        Enemy("Орк-центуріон", 120, 15), Enemy("Скелет-лицар", 150, 12), Enemy("Великий павук-мисливець", 110, 18),
        Enemy("Вогняний елементаль", 130, 20), Enemy("Вервольф", 160, 22), Enemy("Некромант-відступник", 100, 25),

        # БОСИ (Сильні)
        Enemy("Стародавній Гігнат", 400, 25),
        Enemy("Король Скелетів", 350, 35),
        Enemy("Верховний Маг Тіней", 250, 50),
        Enemy("Дракон Пустоти", 600, 40)
    ]
armor_items = [
    # Воїн (7 предметів)
    Item("Сталевий нагрудник", "Воїн", 0, 150, 50),
    Item("Поножі титана", "Воїн", 0, 120, 40),
    Item("Наплічники рунічної сталі", "Воїн", 0, 90, 35),
    Item("Кольчуга майстра", "Воїн", 0, 130, 45),
    Item("Важкі ботфорти", "Воїн", 0, 85, 30),
    Item("Нагрудник світла", "Воїн", 0, 180, 60),
    Item("Мисливські штани", "Воїн", 0, 95, 25),

    # Захисник (7 предметів)
    Item("Щит предків", "Захисник", 0, 200, 80),
    Item("Броня драконячої луски", "Захисник", 0, 300, 100),
    Item("Панцир глибин", "Захисник", 0, 250, 70),
    Item("Шолом легіонера", "Захисник", 0, 110, 45),
    Item("Рукавиці непохитності", "Захисник", 0, 90, 40),
    Item("Шолом темного лицаря", "Захисник", 0, 140, 55),
    Item("Пояс стійкості", "Захисник", 0, 80, 25),

    # Маг (6 предметів)
    Item("Магічний амулет захисту", "Маг", 0, 100, 15),
    Item("Плащ нічної варти", "Маг", 0, 80, 20),
    Item("Корона короля-духа", "Маг", 0, 110, 30),
    Item("Черевики мандрівника", "Маг", 0, 60, 15),
    Item("Бойовий капюшон", "Маг", 0, 70, 20),
    Item("Захисні поручі", "Маг", 0, 50, 25)
]
weapon_items = [
    # Воїн (7 предметів)
    Item("Залізний меч", "Воїн", 25, 0, 0),
    Item("Бойова сокира", "Воїн", 35, 0, 0),
    Item("Спис правосуддя", "Воїн", 40, 0, 0),
    Item("Катана вітру", "Воїн", 38, 0, 0),
    Item("Меч-бастард", "Воїн", 44, 0, 0),
    Item("Ельфійський клинок", "Воїн", 31, 0, 0),
    Item("Меч полум'я", "Воїн", 60, 0, 0),

    # Захисник (7 предметів)
    Item("Молот гніву", "Захисник", 50, 0, 0),
    Item("Палиця велетня", "Захисник", 55, 0, 0),
    Item("Глефа стража", "Захисник", 48, 0, 0),
    Item("Шипована булава", "Захисник", 37, 0, 0),
    Item("Крижаний топір", "Захисник", 52, 0, 0),
    Item("Грозовий тризуб", "Захисник", 58, 0, 0),
    Item("Важкий бардівський ціп", "Захисник", 45, 0, 0),

    # Маг (6 предметів)
    Item("Магічний посох", "Маг", 45, 0, 0),
    Item("Арбалет темряви", "Маг", 42, 0, 0),
    Item("Мисливський лук", "Маг", 30, 0, 0),
    Item("Кинджал вбивці", "Маг", 20, 0, 0),
    Item("Подвійні клинки", "Маг", 32, 0, 0),
    Item("Срібна рапіра", "Маг", 28, 0, 0)
]
accessories_items = [
    # --- Шкода (Damage) ---
    Item("Точильний камінь", "Universal", 5, 0, 0),
    Item("Кільце Сили", "Universal", 8, 0, 0),
    Item("Потерта перев'язь", "Universal", 10, 0, 0),
    Item("Есенція люті", "Universal", 12, 0, 0),
    Item("Наручі мисливця", "Universal", 15, 0, 0),

    # --- Здоров'я (HP) ---
    Item("Медальйон витривалості", "Universal", 0, 20, 0),
    Item("Пояс мандрівника", "Universal", 0, 35, 0),
    Item("Амулет життя", "Universal", 0, 50, 0),
    Item("Окріпша жила", "Universal", 0, 65, 0),
    Item("Кристал стійкості", "Universal", 0, 80, 0),

    # --- Броня (Armor) ---
    Item("Залізний жетон", "Universal", 0, 0, 5),
    Item("Шкіряні наплічники", "Universal", 0, 0, 10),
    Item("Дубовий щиток", "Universal", 0, 0, 15),
    Item("Руна захисту", "Universal", 0, 0, 20),
    Item("Пластинчасті рукавиці", "Universal", 0, 0, 25),

    # --- Гібридні (Mixed) ---
    Item("Знак ветерана", "Universal", 5, 20, 0),
    Item("Оберіг лісу", "Universal", 0, 15, 10),
    Item("Бойовий трофей", "Universal", 7, 0, 7),
    Item("Спадщина предків", "Universal", 10, 10, 10),
    Item("Аметистова підвіска", "Universal", 0, 25, 5)
]

def fight_with_enemy():
    enemy = random.choice(list_of_enemy)


    print(f"УВАГА! на вас напав {enemy.name}")

    while True:
        print("\n")
        my_hero.attack(enemy)
        if enemy.hp <= 0:
            print(f"{enemy.name} переможено!")


            break


        enemy.attack(my_hero)
        if my_hero.hp <= 0:
            print(f"{my_hero.name} пав в бою із {enemy.name}!")
            break
        time.sleep(2)

def found_a_tresure():
    my_chance = random.randint(0,100)

    user_choice = input("Воу! Ви знайшли скарб! Хочете переглянути що там! Ви можете натрапити на міміка!\n"
                        "Відкрити (1) або втекти(2)")

    if user_choice ==2:
        print("Ви втекли від скарбу((")
        return
    else:
        if my_chance < 20:
            tresure = random.choice(accessories_items)
            print(f"Ваша здобич: {tresure.name}"
                  f"\t Бонусна шкода:{tresure.bonus_damage}\n"
                  f"\t Бонусна броня:{tresure.bonus_armor}\n"
                  f"\t Бонусне ХП:{tresure.bonus_hp}\n"
                  f"\t Екіпіювати(1) чи викинути(будь яка кнопка)?")
            user_answer = input()
            if user_answer == "1":
                my_hero.equip_accessorie(tresure)
            else:
                pass
        elif my_chance <= 40:
            pass
        elif my_chance <= 60:
            pass
        elif my_chance <= 80:
            pass
        else:
            pass



print("Вітаємо вас в світі Неверленд! \nДавайте створимо для вас ваш аватар!")
player_name = input("Введіть ім'я вашого аватара:")
print(f"Чудовий вибір, {player_name}")

#Створення персонажа
my_hero = None
while my_hero is None:
    player_class = input("Оберіть ваш клас. Введіть цифру, щоб підтвердити вибір:\n"
        "1) Воїн(100 хп, 10 шкоди)\n"
        "2) Захисник(200 хп, 5 шкоди)\n"
        "3) Маг (80 хп, 15 шкоди)\n")

    if player_class == "1":
        my_hero = Player(player_name, "Воїн",100, 10)
    elif player_class == "2":
        my_hero = Player(player_name, "Захисник", 200, 5)
    elif player_class == "3":
        my_hero = Player(player_name, "Маг", 80, 15)
    else:
        print("Будь ласка, зробіть правильний вибір")


weapon = random.choice(weapon_items)
my_hero.player_info()
my_hero.equip_weapon(weapon)
my_hero.player_info()
input()




situacttion_list = ("Ворог","Відпочинок","Скарб")
while my_hero.hp > 0:
    situacttion = random.choice(situacttion_list)
    if situacttion == "Ворог":
        fight_with_enemy()
    elif situacttion == "Відпочинок":
        my_hero.healing(random.randint(20,80))
    elif situacttion == "Скарб":
        found_a_tresure()
    input("Для наступного кроку натисніть Ентер!")



