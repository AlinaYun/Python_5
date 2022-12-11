# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. 
# Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Подумайте как наделить бота ""интеллектом""

from random import randint

total_number_of_candies = 150 #всего конфет
number_to_take = 28 # кол-во конфет, которые можно забрать за 1 ход


print (f"Привет! Давай сыграем в игру: на столе лежит {total_number_of_candies} конфет(а). За один ход можно забрать не более, чем {number_to_take} штук. Все конфеты оппонента достаются сделавшему последний ход.")
user_choice = int(input("Подбросим монету, определим кто ходит первый. Введи 0, чтоб выбрать орла и 1, чтоб выбрать решку. "))

def define_who_first():
    who_first = randint(0,1)
    if who_first ==  user_choice:
        print ("Ты ходишь первым")
        return 1
    else:
        print ("я хожу первым")
        return 2

def game (turn):    
    global total_number_of_candies
    global number_to_take
    while total_number_of_candies > number_to_take:
        if turn == 1:
            while True:
                user_take = int(input(f"Твой ход: сколько конфет берешь? (введи число от 1 до {number_to_take}) "))
                if 1 <= user_take <= number_to_take:
                    break
                else: 
                    print ("Введено некорректное значение")
            total_number_of_candies -= user_take
            print (f"Осталось {total_number_of_candies} конфет")
            turn = 2
        elif turn == 2:
            #bot_take = randint(1,number_to_take) # компьютер берет рандомное число 
            if total_number_of_candies % (number_to_take + 1) == 0:
                bot_take = randint(1,number_to_take)
            else:
                bot_take = (total_number_of_candies % (number_to_take + 1))
            total_number_of_candies -= bot_take
            print(f"Мой ход: я беру {bot_take} конфет(у/ы). Осталось {total_number_of_candies} конфет.")
            turn = 1
    if turn == 1:
        print ("Ты забираешь оставшиеся конфеты, ты выйграл! Поздравляю!")
    else:
        print (f"Я забираю оставшиеся {total_number_of_candies}. Я выйграл! ")

game(define_who_first())





