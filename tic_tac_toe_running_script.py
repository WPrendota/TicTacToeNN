from report_generator import *
from argparse import ArgumentParser
import re
from tic_tac_toe import TicTacToe


# The argument parser
def args_parser():
    args = ArgumentParser(description="The Tic Tac Toe Game.")
    args.add_argument('-e', action="store_true", help="The TicTacToe game: easy bot.")
    args.add_argument('-s', action="store_true", help="The TicTacToe game: strong bot.")
    args.add_argument('-c', nargs=2, type=int,
                      help="The data gathering mode: Random Computer Player vs Random Computer Player,")
    args.add_argument('-d', nargs=2, type=int, help="The data gathering mode: Random Computer Player vs QRL Player,")
    args.add_argument('-t', nargs=2, type=int, help="The data gathering mode: QRL Player vs QRL Player.")

    return args.parse_args()


# Check which game was chosen
def chosen_game_mode(args):
    # Game mode chooser and running
    if args.e:
        return 1

    elif args.s:
        return 2

    elif args.c:
        return 3

    elif args.d:
        return 4

    elif args.t:
        return 5
    else:
        print("Please choose a game mode:")
        print("-e for The TicTacToe game: easy bot.")
        print("-s for The TicTacToe game: strong bot.")
        print("-c for The data gathering mode: Random Computer Player vs Random Computer Player,")
        print("-d for The data gathering mode: Random Computer Player vs QRL Player,")
        print("-t for The data gathering mode: QRL Player vs QRL Player.")
        return 0


# The data loader from the file
def load_data(file_name):
    file_data = ''

    with open(file_name, 'r') as f:
        file_data = f.read().splitlines()

    file_data_list = []
    file_label_list = []

    for row in file_data:
        tmp = row.split(', ')
        list = []
        for letter in tmp[0]:
            if letter.isdigit():
                list.append(int(letter))
        file_data_list.append(list)

    for row in file_data:
        tmp = row.split(', ')
        list = re.findall(r"[-+]?\d*\.\d+|\d+", tmp[1])
        file_label_list.append(list)

    return file_data_list, file_label_list


# Function for collecting training data
def gather_data(game_mode, game_total_count, data_type_name):
    data = []

    for x in range(1, game_total_count, 1):
        data.append(TicTacToe(game_mode, data_type_name).run_game())

        if x % 10 == 0:
            print("Iteration: {}".format(x))

    return data


# Modify data
def separate_data(data_list):
    separated_data_list = []
    separated_label_list = []

    for data in data_list:
        print(data_list)
        for board in data:
            separated_data_list.append(board[0])
            separated_label_list.append(board[1])

    data_array_list = np.array(separated_data_list)
    label_array_list = np.array(separated_label_list)

    return data_array_list, label_array_list


def data_gathering(game_mode, test_iteration_number=0, train_iteration_number=0):
    # Create training data
    if train_iteration_number != 0:
        training_data = gather_data(game_mode, train_iteration_number, 'training')

        # Calculate and plot data (training_data)
        plot_labels(training_data, "player_qrl_1_training", train_iteration_number)

    # Create testing data
    if test_iteration_number != 0:
        test_data = gather_data(game_mode, test_iteration_number, 'test')

        # Calculate and plot data (training_data)
        plot_labels(test_data, "player_qrl_1_test", test_iteration_number)


def run_script(game_mode, arg_1=0, arg_2=0):
    # Run game:
    if game_mode == 1:
        ttt = TicTacToe(1)
        ttt.run_game()
    elif game_mode == 2:
        ttt = TicTacToe(2)
        ttt.run_game()
    elif game_mode == 3:
        # The number of test and training data to collect
        data_gathering(game_mode, arg_1, arg_2)
    elif game_mode == 4:
        # The number of test and training data to collect
        data_gathering(game_mode, arg_1, arg_2)
    elif game_mode == 5:
        # The number of test and training data to collect
        data_gathering(game_mode, arg_1, arg_2)
    else:
        print("Error. Please use -h for help.")


if __name__ == '__main__':
    game_mode = chosen_game_mode(args_parser())

    # Run game:
    if game_mode == 1:
        ttt = TicTacToe(1)
        ttt.run_game()
    elif game_mode == 2:
        ttt = TicTacToe(2, 'training')
        ttt.run_game()
    elif game_mode == 3:
        # The number of test and training data to collect
        data_gathering(game_mode, args_parser().c[0], args_parser().c[1])
    elif game_mode == 4:
        # The number of test and training data to collect
        data_gathering(game_mode, args_parser().d[0], args_parser().d[1])
    elif game_mode == 5:
        # The number of test and training data to collect
        data_gathering(game_mode, args_parser().t[0], args_parser().t[1])
    else:
        print("Error. Please use -h for help.")
