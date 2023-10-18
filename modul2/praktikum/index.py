import random
board = []
player_position = []
enemy_position = []
matrix = []

def main(): 
    global board
    global player_position
    global enemy_position
    global matrix

    approvedCondition = True
    counterCondition = 0

    matrix.append(int(input("Masukan Baris : "))) 
    matrix.append(int(input("Masukan Kolom : ")))

    player_position = set_position(matrix)
    enemy_position = set_position(matrix)

    board = set_enemy(set_player(set_board(matrix), player_position), enemy_position)
    get_board(board)

    while(approvedCondition):
        user_input = str(input("New Possition (Y/N)? "))

        if(user_input == "Y"):
            player_position = set_position(matrix)
            enemy_position = set_position(matrix)
            board = set_enemy(set_player(set_board(matrix), player_position), enemy_position)
            get_board(board)
            counterCondition += 1
        if(user_input == "N" or counterCondition == 3):
            approvedCondition = False

    player_position = player_move(player_position)

    board = set_enemy(set_player(set_board(matrix), player_position), enemy_position)
    get_board(board)

    val = "You Win" if player_position == enemy_position else "You Sucks"
    print(val)

def set_board(matrix):
    board = []
    board_column = []
    board_pattern = "-"
    
    for x in range(matrix[0]):
        for y in range(matrix[1]):
            board_column.append(board_pattern)
        board.append(board_column)
        board_column = []

    return board
    
def get_board(board):
    get_column = ""
    for x, y in enumerate(board): 
        for i in y:
            get_column += (i+" ")
        print(get_column)
        get_column = ""

def set_player(board, user):
    game_column = []
    game_board = []

    for x, y in enumerate(board):
        if (user[0] == x):
            for x1, y1 in enumerate(y):
                if(user[1] == x1):
                    y1 = "A"
                game_column.append(y1)
            game_board.append(game_column)
                
        else:
            game_board.append(y)
    
    return game_board

def set_enemy(board, enemy):
    game_column = []
    game_board = []

    for x, y in enumerate(board):
        if (enemy[0] == x):
            for x1, y1 in enumerate(y):
                if(enemy[1] == x1):
                    if(y1 == "A"):
                        y1 = "A"
                    else:
                        y1 = "O"
                game_column.append(y1)
            game_board.append(game_column)
                
        else:
            game_board.append(y)
    
    return game_board

def set_position(matrix): return [random.randrange(0, matrix[0] - 1), random.randrange(0, matrix[1] - 1)]

def player_move(user):
    test = []
    user_input = str(input("Masukan Movement : "))

    for i in user_input:
        if(i == "w"):user[0] -= 1
        if(i == "a"):user[1] -= 1
        if(i == "s"): user[0] += 1
        if(i == "d"): user[1] += 1
    
    return user

main()