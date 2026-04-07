import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board):
    print()

    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()


def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()

    return (symbol, 'O' if symbol == 'X' else 'X')


def player_move(board, symbol):
    while True:
        try:
            move = int(input(Fore.GREEN + "Enter your move (1-9): " + Style.RESET_ALL))
            if move in range(1, 10) and board[move - 1].isdigit():
                board[move - 1] = symbol
                break
            else:
                print(Fore.RED + "Invalid move. Try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a number between 1 and 9." + Style.RESET_ALL)


def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            copy = board.copy()
            copy[i] = ai_symbol
            if check_win(copy, ai_symbol):
                board[i] = ai_symbol
                return

    for i in range(9):
        if board[i].isdigit():
            copy = board.copy()
            copy[i] = player_symbol
            if check_win(copy, player_symbol):
                board[i] = ai_symbol
                return

    if board[4].isdigit():
        board[4] = ai_symbol
        return

    corners = [i for i in [0, 2, 6, 8] if board[i].isdigit()]
    if corners:
        board[random.choice(corners)] = ai_symbol
        return

    possible_moves = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(possible_moves)] = ai_symbol


def check_win(board, symbol):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def check_full(board):
    return all(not spot.isdigit() for spot in board)


def tic_tac_toe():
    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!" + Style.RESET_ALL)
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        board = [str(i) for i in range(1, 10)]
        player_symbol, ai_symbol = player_choice()

        turn = random.choice(['Player', 'AI'])
        print(Fore.YELLOW + f"{turn} will go first!" + Style.RESET_ALL)

        game_on = True

        while game_on:
            display_board(board)

            if turn == 'Player':
                player_move(board, player_symbol)

                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"🎉 Congratulations {player_name}, you win!" + Style.RESET_ALL)
                    game_on = False

                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_on = False
                else:
                    turn = 'AI'

            else:
                print(Fore.BLUE + "AI is making a move..." + Style.RESET_ALL)
                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "😈 AI wins! Better luck next time." + Style.RESET_ALL)
                    game_on = False

                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_on = False
                else:
                    turn = 'Player'

        play_again = input(Fore.GREEN + "Play again? (y/n): " + Style.RESET_ALL).strip().lower()
        if play_again not in ['y', 'yes']:
            print(Fore.CYAN + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    tic_tac_toe()