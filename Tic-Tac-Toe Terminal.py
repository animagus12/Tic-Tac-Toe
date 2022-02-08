import sys

board = {
    1: ("_"), 2: ("_"), 3: ("_"),
    4: ("_"), 5: ("_"), 6: ("_"),
    7: ("_"), 8: ("_"), 9: ("_")
}

loc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in range(1, 10, 3):
    print("       |       |")
    print("   " + board[row] + "   |   " +
          board[row + 1] + "   |   " + board[row + 2])
    print("       |       |")


def update(choice, symbol):
    board[choice] = symbol

    for row in range(1, 10, 3):
        print("       |       |")
        print("   " + board[row] + "   |   " +
              board[row + 1] + "   |   " + board[row + 2])
        print("       |       |")
    loc_list.remove(choice)
    checker()


def checker():
    if board[1] == board[2] == board[3] == symbol[0] or board[4] == board[5] == board[6] == symbol[0] or board[7] == board[8] == board[9] == symbol[0]:
        print("Player 1 won!")
        sys.exit()
    elif board[1] == board[2] == board[3] == symbol[1] or board[4] == board[5] == board[6] == symbol[1] or board[7] == board[8] == board[9] == symbol[1]:
        print("Player 2 won!")
        sys.exit()
    if board[1] == board[4] == board[7] == symbol[0] or board[2] == board[5] == board[8] == symbol[0] or board[3] == board[6] == board[9] == symbol[0]:
        print("Player 1 won!")
        sys.exit()
    elif board[1] == board[4] == board[7] == symbol[1] or board[2] == board[5] == board[8] == symbol[1] or board[3] == board[6] == board[9] == symbol[1]:
        print("Player 2 won!")
        sys.exit()
    if board[1] == board[5] == board[9] == symbol[0] or board[3] == board[5] == board[7] == symbol[0]:
        print("Player 1 won!")
        sys.exit()
    elif board[1] == board[5] == board[9] == symbol[1] or board[3] == board[5] == board[7] == symbol[1]:
        print("Player 2 won!")
        sys.exit()
    if "_" not in board.values():
        print("Draw!")
        sys.exit()


def player(player1_symbol):
    choice = int(input("Player 1 location b/w 1-9: "))
    update(choice, player1_symbol)


def player2(player2_symbol):
    choice = int(input("Player 2 location b/w 1-9: "))
    update(choice, player2_symbol)


p1_symbol = ''
while p1_symbol != 'X' and p1_symbol != 'O':
    p1_symbol = input("Player 1: Choose 'X' or 'O'?: ").upper()
    if p1_symbol == 'X':
        symbol = ('X', 'O')
    else:
        symbol = ('O', 'X')

while "_" in board.values():
    player(symbol[0])
    player2(symbol[1])
print("Draw!")
