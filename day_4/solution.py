import copy


def read_input():
    with open('data.txt') as f:
        _input_data = [line.rstrip() for line in f]
        return _input_data


data = read_input()

is_first_line = True
bingo_boards = {}
bingo_boards_index = -1

# generate bingo_boards
for line in data:
    if is_first_line:
        winning_numbers = line.split(',')
        is_first_line = False
    elif line == "":
        bingo_boards_index += 1
        bingo_board_list = []
        bingo_boards[bingo_boards_index] = bingo_board_list
    else:
        bingo_board_list.append(list(line.split()))

bingo_boards_copy = copy.deepcopy(bingo_boards)


def calculate_board(board_key):
    sum = 0
    board = bingo_boards.get(board_key)
    for i in board:
        for ii in i:
            if ii != 'X':
                sum += int(ii)

    return sum


def check_bingo_board(board_key):
    board = bingo_boards.get(board_key)
    # row
    for i in range(len(board)):
        checked = 0
        for ii in range(len(board)):
            if board[i][ii] == 'X':
                checked += 1
                if checked == len(board):
                    sum = calculate_board(board_key)
                    return sum

    # column
    for i in range(len(board)):
        checked = 0
        for ii in range(len(board)):
            if board[ii][i] == 'X':
                checked += 1
                if checked == len(board):
                    sum = calculate_board(board_key)
                    return sum


def mark_boards():
    for number in winning_numbers:
        for key, value in bingo_boards.items():
            for current_list in value:
                for i in range(len(current_list)):
                    if current_list[i] == number:
                        current_list[i] = 'X'
                        winner = check_bingo_board(key)
                        if (winner):
                            print(number)
                            print(winner)
                            print(int(winner)*int(number))
                            return


mark_boards()
