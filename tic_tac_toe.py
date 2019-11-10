import numpy as np
from computer_player import ComputerPlayer
from player_qrl import PlayerQRL
from game_board import GameBoard


class TicTacToe:

    # The game initialization
    def __init__(self, game_number, file_name=None):
        self.winner = 0     # The winner
        self.board_size = 3  # The board size
        self.game_number = game_number # The game number
        self.game_board = GameBoard(self.board_size)  # Board creation
        self.file_name = file_name

        # Computer Player move - easy bot
        if game_number == 1:
            self.computer_player = ComputerPlayer()  # The Computer Player
        # Computer Player move - strong bot
        elif game_number == 2:
            self.computer_player = PlayerQRL(1, 0.1, 0.9, 0.7, game_number, 1)  # The QRL Computer Player
        elif game_number == 3:
            self.player_list = []

            # Add 1st Player:
            self.player_list.append(ComputerPlayer())

            # Add 2nd Player:
            self.player_list.append(ComputerPlayer())

            # Load saved players data:
            load_players_stats(self.player_list, file_name)
        elif game_number == 4:
            self.player_list = []

            # Add 1st Player:
            # Parameters: mark, learning rate, discount, exploration rate
            self.player_list.append(PlayerQRL(1, 0.1, 0.9, 0.7, game_number, 1))

            # Add 2nd Player:
            self.player_list.append(ComputerPlayer())

            # Load saved players data:
            load_players_stats(self.player_list, file_name)
        elif game_number == 5:
            self.player_list = []

            # Add 1st Player:
            # Parameters: mark, learning rate, discount, exploration rate
            self.player_list.append(PlayerQRL(-1, 0.1, 0.9, 0.7, game_number, 1))

            # Add 2nd Player:
            self.player_list.append(PlayerQRL(1, 0.1, 0.9, 0.7, game_number, 1))

            # Load saved players data:
            load_players_stats(self.player_list, file_name)

    # The game running
    def run_game(self):
        while True:
            if self.game_number == 1 or self.game_number == 2:
                print("(Input format: '11')")
                print("Your move:")
                move_input_raw = input()
                print(move_input_raw)

                if self.game_number == 1 or 2:
                    if self.check_input_format(move_input_raw):
                        human_move = (int(move_input_raw[0]), int(move_input_raw[1]))

                        if self.check_input_range(human_move):
                            if self.check_next_move(human_move):
                                self.game_board.set_pawn(human_move[0], human_move[1], 1)

                                # Check if winner
                                if self.validate(-1, 1):
                                    if self.winner == 3:
                                        print("It is a Tie!")
                                    else:
                                        print("The winner is: {}".format(self.winner))

                                    if self.game_number == 2:
                                        print(self.computer_player.q_tables.values())
                                        # Update Player Q-Table
                                        self.computer_player.update(self.winner)
                                        # Print player statistics
                                        # print_game_stats(board, player_list, game_number)

                                        # Save players statistics into separate '.txt' file
                                        save_players_stats([self.computer_player], 'training')

                                        # Export data to text file
                                        export_data_to_text_file([self.computer_player], 'training')
                                    break

                                #  Check if tie
                                if not self.check_if_board_is_full:
                                    if self.validate(-1, 1):
                                        print("The winner is: {}".format(self.winner))
                                        print(self.computer_player.q_tables.values())
                                    break

                                # Computer Player move
                                if self.game_number == 1:
                                    while True:
                                        computer_move = self.computer_player.set_pawn(self.game_board)
                                        if self.check_next_move(computer_move):
                                            self.game_board.set_pawn(computer_move[0], computer_move[1], -1)
                                            break




                                if self.game_number == 2:
                                    computer_move = self.computer_player.set_pawn(self.game_board)

                                    if self.check_next_move(computer_move):
                                        self.game_board.set_pawn(computer_move[0], computer_move[1], -1)





                                # Check if winner
                                if self.validate(-1,1):
                                    print(self.game_board.get())
                                    if self.winner == 3:
                                        print("It is a Tie!")
                                    else:
                                        print("The winner is: {}".format(self.winner))

                                    if self.game_number == 2:
                                        print(self.computer_player.q_tables.values())
                                    break
                            else:
                                print("Position taken! Please choose empty field.")
                        else:
                            print("Wrong move. Try again.")
                            continue

                        print(self.game_board)
                    else:
                        print("Wrong move. Try again.")


            elif self.game_number == 3:
                while True:
                    easy_bot_move = self.player_list[1].set_pawn(self.game_board)
                    if self.check_next_move(easy_bot_move):
                        self.game_board.set_pawn(easy_bot_move[0], easy_bot_move[1], -1)
                        break

                # Check if winner
                if self.validate(-1, 1):

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner

                while True:
                    easy_bot_2_move = self.player_list[0].set_pawn(self.game_board)
                    if self.check_next_move(easy_bot_2_move):
                        self.game_board.set_pawn(easy_bot_2_move[0], easy_bot_2_move[1], 1)
                        break

                # Check if winner
                if self.validate(-1, 1):

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner


            elif self.game_number == 4:
                while True:
                    easy_bot_move = self.player_list[1].set_pawn(self.game_board)
                    if self.check_next_move(easy_bot_move):
                        self.game_board.set_pawn(easy_bot_move[0], easy_bot_move[1], -1)
                        break

                # Check if winner
                if self.validate(-1, 1):
                    #print(self.game_board.get())
                    #print("The winner is: {}".format(self.winner))

                    # Update QRLPlayer Q-Table
                    self.player_list[0].update(self.winner)

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner

                learning_bot_move = self.player_list[0].set_pawn(self.game_board)
                #print(learning_bot_move)
                if self.check_next_move(learning_bot_move):
                    self.game_board.set_pawn(learning_bot_move[0], learning_bot_move[1], 1)

                # Check if winner
                if self.validate(-1, 1):
                    #print(self.game_board.get())
                    #print("The winner is: {}".format(self.winner))

                    # Update QRLPlayer Q-Table
                    self.player_list[0].update(self.winner)

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner


            elif self.game_number == 5:
                learning_bot_move = self.player_list[0].set_pawn(self.game_board)
                # print(learning_bot_move)
                if self.check_next_move(learning_bot_move):
                    self.game_board.set_pawn(learning_bot_move[0], learning_bot_move[1], -1)

                # Check if winner
                if self.validate(-1, 1):
                    #print(self.game_board.get())
                    #print("The winner is: {}".format(self.winner))

                    # Update QRLPlayer Q-Table
                    self.player_list[0].update(self.winner)
                    self.player_list[1].update(self.winner)

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner

                learning_bot_1_move = self.player_list[1].set_pawn(self.game_board)
                #print(learning_bot_move)
                if self.check_next_move(learning_bot_1_move):
                    self.game_board.set_pawn(learning_bot_1_move[0], learning_bot_1_move[1], 1)

                # Check if winner
                if self.validate(-1, 1):
                    #print(self.game_board.get())
                    #print("The winner is: {}".format(self.winner))

                    # Update QRLPlayer Q-Table
                    self.player_list[0].update(self.winner)
                    self.player_list[1].update(self.winner)

                    # Save players statistics into separate '.txt' file
                    save_players_stats(self.player_list, self.file_name)

                    # Export data to text file
                    export_data_to_text_file(self.player_list, self.file_name)

                    return self.winner


    # Checking input format
    def check_input_format(self, input_data):
        return True if len(input_data) == 2 else False

    # Checking move range
    def check_input_range(self, move):
        return True if self.board_size > move[0] >= 0 and self.board_size > move[1] >= 0 else False

    # Checking game board field status for the next move
    def check_next_move(self, move):
        return True if self.game_board.get_value(move[0], move[1]) == 0 else False

    # Checking if board is full
    def check_if_board_is_full(self):
        return True if 0 in self.game_board.get() else False

    def check_columns(self, player):
        # Column are rows in the transposed list
        for column in zip(*self.game_board.get()):
            if abs(self.count_character(player, column)) == 3:
                return player
            if abs(self.count_character(player, column)) == 3:
                return player

        return False

    def check_rows(self, player):
        for row in self.game_board.get():
            if abs(self.count_character(player, row)) == 3:
                return player
            if abs(self.count_character(player, row)) == 3:
                return player

        return False

    def check_diagonals(self, player):
        # Wins if there is only one type of value in the first diagonal
        # (Numpy diag returns values on diagonal of the array).
        if abs(self.count_character(player, np.diag(self.game_board.get()))) == 3:
            return player
        if abs(self.count_character(player, np.diag(self.game_board.get()))) == 3:
            return player

        # Wins if there is only one type of value in the second diagonal (Numpy diag returns values of diagonal
        # - Numpy fliplr changes values from left to right of the array).
        if abs(self.count_character(player, np.diag(np.fliplr(self.game_board.get())))) == 3:
            return player
        if abs(self.count_character(player, np.diag(np.fliplr(self.game_board.get())))) == 3:
            return player

        return False

    # Winner finding
    def validate(self, player_1, player_2):

        if self.check_columns(player_1):
            self.winner = player_1
            return True

        if self.check_columns(player_2):
            self.winner = player_2
            return True

        if self.check_rows(player_1):
            self.winner = player_1
            return True

        if self.check_rows(player_2):
            self.winner = player_2
            return True

        if self.check_diagonals(player_1):
            self.winner = player_1
            return True

        if self.check_diagonals(player_2):
            self.winner = player_2
            return True

        counter = 0
        for row in self.game_board.get():
            for value in row:
                if value == 0:
                    counter = counter + 1
        if counter == 0:
            self.winner = 3
            return True

    # Count character in the word
    def count_character(self, character, word):
        return sum(character for word_character in word if character == word_character)

    def set_pawn(self, position_x, position_y, pawn):
        if not self.is_valid_move(position_x, position_y):
            raise Exception("Pawn not valid position.")
        self.game_board.get()[position_x][position_y] = pawn

    def is_valid_move(self, position_x, position_y):
        return False if int(self.game_board.get()[position_x][position_y]) == 1 or int(
            self.game_board.get()[position_x][position_y]) == 2 else True

    def has_next_move(self):
        return np.any(self.game_board.get())


# Assigned tuple with data from the list and value. Return new list with 2 value tuple for each list index
def correct_data_format(data_list, winner):
    corrected_data_list = []

    for data in data_list:
        corrected_data_list.append((data, winner))

    return corrected_data_list


# Save players statistics
def save_players_stats(player_list, data_type_name):
    for player in player_list:
        if isinstance(player, PlayerQRL):
            player.save_q_table(data_type_name)


# Load players statistics
def load_players_stats(player_list, file_name):
    for player in player_list:
        if isinstance(player, PlayerQRL):
            player.load_q_table('q_table_' + str(player.mark) + '_' + file_name + '.pickle')
            player.load_q_values('q_values_' + str(player.mark) + '_' + file_name + '.pickle')


# Export state-action data to text file
def export_data_to_text_file(player_list, name):
    for player in player_list:
        if isinstance(player, PlayerQRL):
            player.export_q_table(name)


# Print each game data
def print_game_stats(board, player_list, game_number):
    print("\n")
    print('Game number: ' + str(game_number))
    print("Board: ")

    print(board.get_board_values())
    print("Winner: " + str(board.get_winner()))

    print("\n")
    print("Player 1 Q-Table: ")
    print(player_list[0].get_q_table())
    print("Player 2 Q-Table: ")
    print('-----------------------------------')