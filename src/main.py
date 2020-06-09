from src.entity import *
from src.location import *

GLOBAL_DEBUG = False  # Currently has no effect, although its behavior must be pretty trivial
GLOBAL_DIFFICULTY = 1


def main():
    print("Добро пожаловать!")
    player_name = input("Как тебя зовут?: ")
    print("Очень приятно,", player_name)
    name_annoyance = 0
    prompt_annoyance = 0
    while(True):
        decision = input('''1. Новая игра
2. Я все-таки не ''' + player_name + '''
3. Выход
Ваша цифра?: ''')
        if decision is '1':
            break
        elif decision is '2':
            if name_annoyance == 2:
                print("Хватит менять имя! Определись уже.")
                name_annoyance = 0
            else:
                player_name = input("Хорошо. А кто тогда? ")
                print("Очень приятно,", player_name)
                name_annoyance += 1
        elif decision is '3':
            print("Всего хорошего!")
            exit(0)
        else:
            if prompt_annoyance == 2:
                print("Это что, настолько сложно?" +
                      " Просто напиши цифру из тех что видишь на экране, больше ничего не нужно")
                prompt_annoyance = 0
            else:
                print("Не понял. Давай еще разок")
                prompt_annoyance += 1

    while True:
        decision = input('''Выберите уровень сложности:
1. Легкий
2. Нормальный
3. Сложный
4. Ультранасилие
?: ''')
        dic = {'1': 0.8, '2': 1, '3': 1.2, '4': 1.4}
        if decision in dic.keys():
            main.GLOBAL_DIFFICULTY = dic[decision]  # Currently has no effect
            break;
    print("Игра началась!")
    player = Player(player_name)
    current_location = first_floor
    player.move(current_location)

    # Game loop
    # Tick sequence:
    # 1. Request action
    # 2. If move to other hub location (i.e. floor) - change location
    # 3. If move to fight location (i.e. auditory, boss) - fetch entity, enter fight loop
    # 4. If shop available and requested - shop

    # Fight loop
    # 0. Set in_fight = True, may not be necessary though
    # 1. Request and execute player action
    # 1a. except Dead - player won, give money, break
    # 2. Select and execute entity action
    # 2a. except Dead - player lost, break
    # 3. Tick player
    # 4. Tick entity
    in_fight = False
    while True:
        print("Текущая локация: ")


if __name__ == "__main__":
    main()
