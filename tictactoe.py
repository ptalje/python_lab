#init_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#curr_board = init_board
has_winner = False
game_on = True


def display_board(input_board):
    line_separator = '--------------------'
    horizontal_separator = '     |       |     '
    sign_positions = [1, 3, 5]
    vert_positions = [0, 2, 4, 6]
    for i in range(10):
        if i in vert_positions:
            print(line_separator)
        elif i in sign_positions:
            if i == 1:
                repl_string = horizontal_separator[0:2] + input_board[7] + horizontal_separator[3:]
                repl_string = repl_string[0:9] + input_board[8] + repl_string[10:]
                repl_string = repl_string[0:16] + input_board[9] + repl_string[17:]
            elif i == 3:
                repl_string = horizontal_separator[0:2] + input_board[4] + horizontal_separator[3:]
                repl_string = repl_string[0:9] + input_board[5] + repl_string[10:]
                repl_string = repl_string[0:16] + input_board[6] + repl_string[17:]
            elif i == 5:
                repl_string = horizontal_separator[0:2] + input_board[1] + horizontal_separator[3:]
                repl_string = repl_string[0:9] + input_board[2] + repl_string[10:]
                repl_string = repl_string[0:16] + input_board[3] + repl_string[17:]
            print(repl_string)


def clear_screen():
    print('\n' * 100)


def show_board_info():
    position_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('Grid positions. Select a number to place your marker.')
    display_board(position_board)
    print('\n####################################################\n')


def player_input():
    valid_markers = ['X', 'O']
    input_string = ''
    while input_string not in valid_markers:
        input_string = input('What marker do you want? Enter X or O: ')
    return input_string


def choose_starter():
    import random
    if random.randint(0, 1) == 0:
        return 2
    return 1


def place_marker(board, marker, position):
    board[position] = marker
    return board


def position_check(board, position):
    if board[position] in ['X', 'O']:
        print('Hey, that spot is taken by {}. Pick another one!'.format(board[position]))
        return False
    return True


def calculate_win(input_board, marker):
    valid_combinations = [(1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7)]
    for_the_win = False
    for valid in valid_combinations:
        if input_board[valid[0]] == marker and input_board[valid[1]] == marker and input_board[valid[2]] == marker:
            print('Looks like we have a winner. Congratulations player ' + str(input_board[valid[0]]) + '!')
            for_the_win = True
            display_board(input_board)
            break
    if ' ' not in set(input_board):
        display_board(input_board)
        print('Damn, it was a tie. No winner')
        return 'tie'
    return for_the_win


def replay():
    continue_play = ''
    while continue_play not in ['Y', 'N']:
        continue_play = input('Play again? Y/N')
    if continue_play == 'Y':
        return True
    elif continue_play == 'N':
        return False


while game_on:
    curr_board = [' '] * 10
    p1_marker = player_input()
    p2_marker = 'O' if p1_marker == 'X' else 'X'
    starter = choose_starter()
    curr_marker = p1_marker if starter == 1 else p2_marker
    print('Player {} gets to start! Your marker is {}'.format(starter, curr_marker))

    while not has_winner:
        clear_screen()
        show_board_info()
        display_board(curr_board)
        next_marker = p2_marker if curr_marker == p1_marker else p1_marker
        desired_pos = input('Ok player {}, pick a free spot for your marker: '.format(curr_marker))
        valid_position = position_check(curr_board, int(desired_pos))
        if not valid_position:
            continue
        curr_board = place_marker(curr_board, curr_marker, int(desired_pos))
        game_over = calculate_win(curr_board, curr_marker)
        if game_over == 'tie':
            if not replay():
                game_on = False
                break
        else:
            has_winner = game_over
            curr_marker = next_marker

    if not replay():
        game_on = False
    else:
        has_winner = False

