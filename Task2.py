#Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))
wins_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1,4,7), (2, 5, 8), (3, 6, 9)]

def get_board():
    for i in range (3):
        print (board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])
    

def user_input (user_char):
    while True:
        user_turn = input("Выберите число, чтоб поставить туда " + user_char + ": ")
        if user_turn not in "123456789":
            print("Ошибка, попробуйте еще раз")
            continue
        else:
            user_turn = int(user_turn) 
        if str(board[user_turn - 1]) in "XO":
            print("Позиция уже занята. Попробуйте еще раз")
            continue
        else:
            board[user_turn - 1] = user_char
            break

def check_win():
    for i in wins_combination:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False

counter = 0
while True:
    get_board()
    if counter % 2 == 0:
        user_input('X')
    else:
        user_input('O')
    if counter > 3:
        winner = check_win()
        if winner:
            get_board()
            print (winner, "Выйграл")
            break
    counter = counter + 1
    if counter > 8:
        get_board()
        print("Ничья!")
        break