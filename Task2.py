# 2.    Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""

import random


def player_round(max_num, num, player):
    take_candy = -1
    while 0 > take_candy or take_candy > max_num or take_candy > num:
        take_candy = int(
            input(f'Сколько конфет из {num} возмет игрок {player}? '))
        if take_candy > max_num:
            print(
                f'Не надо быть жадным - максимально количество конфет которые можно взять -  {max_num}!')
        elif take_candy > num:
            print(f'Осталось всего {num} кофет!')
        elif take_candy == 0:
            print(f'Надо взять минимум одну конфету!')
    return take_candy


def bot_round(max_num, num):
    if num <= max_num:
        take_candy = num
    elif num > max_num and num - max_num <= max_num + 1:
        take_candy = num - max_num - 1
    else:
        take_candy = num - (num // (max_num + 1)) * (max_num + 1) + 1
    take_candy = 1 if take_candy == 0 or take_candy > max_num else take_candy
    print(f'Бот берет {take_candy} конфет(у).')
    return take_candy


candy = 201
max_candy = 28
print(f'  На столе лежит {candy} конфет(а). Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {max_candy} конфет. \
Все конфеты оппонента достаются сделавшему последний ход. Если хотите играть с ботом - введите имя "bot".')
p_name = []
p_name.append(input("Имя первого игрока: "))
p_name.append(input("Имя второго игрока: "))

in_game_player = random.randint(0, 1)

print(f'Первым ходит игрок {p_name[in_game_player]}')

game_candy = candy

while game_candy > 0:
    if 'bot' not in p_name[in_game_player]:
        game_candy -= player_round(max_candy, game_candy,
                                   p_name[in_game_player])
    else:
        game_candy -= bot_round(max_candy, game_candy)
    print(f'Осталось конфет - {game_candy}.')
    in_game_player = int(not bool(in_game_player))
print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')
