import os
import pickle
import numpy as np


class PlayerQRL:
    # Players mark
    mark = 0

    # Players last move coordinates
    previous_move = (-1, -1)

    def __init__(self, mark, learning_rate, discount, exploration_rate, game_count, reward):
        self.mark = mark
        self.q_tables = {}
        self.q_values = {}

        self.q_table_v = {}
        self.moves = []
        self.state_action_table = []
        self.action_boards = []
        self.learning_rate = learning_rate
        self.discount = discount
        self.exploration_rate = exploration_rate
        self.exploration_rate_delta = exploration_rate/game_count
        self.action_mark = 2
        self.reward = reward
        self.first_move = True

    def __str__(self):
        return str(self.mark)

    def set_previous_move(self, move):
        self.previous_move = move

    def get_q_tables(self):
        return self.q_tables

    def set_pawn(self, current_board):
        current_board_values = current_board.get()
        q_values = self.get_q_values(current_board_values.tobytes(), current_board_values)
        q_val = q_values.copy()

        counter = 0
        while True:
            move = np.argmax(q_values)  # arg position

            board_1d = np.ravel(current_board_values)

            if board_1d[move] == 0:
                #print(move)
                for i in range(3):
                    for j in range(3):
                        x = i + 3 * j
                        if x == move:

                            self.moves.append((current_board_values.tobytes(), move))

                            return j, i
            else:
                q_values[move] = - 1

            counter = counter + 1
            if counter > 5:
                exit(0)

    def set_q_value(self, reward):
        next_max_q = -1
        key = False

        for move in self.moves[::-1]:
            q_val = self.get_q_values(move[0])

            if not key:
                q_val[move[1]] = reward
                self.q_values[move[0]] = reward
                key = True
                continue

            if reward < 0 and next_max_q < 0:
                next_max_q = min(q_val)
                q_val[move[1]] = q_val[move[1]] * (
                        1.0 - self.learning_rate) - self.learning_rate * self.discount * next_max_q
                self.q_values[move[0]] = q_val[move[1]]
            else:
                next_max_q = max(q_val)
                q_val[move[1]] = q_val[move[1]] * (
                            1.0 - self.learning_rate) + self.learning_rate * self.discount * next_max_q
                self.q_values[move[0]] = q_val[move[1]]

    def get_q_values(self, entry, board=None):
        if entry in self.q_tables.keys():
            # Check if exists
            q_values = self.q_tables[entry]
        else:
            # Creates new table
            q_values = [0.6 for x in range(9)]
            board_1d = np.ravel(board)

            for x in range(9):
                if board_1d[x] == 1:
                    q_values[x] = -10
                if board_1d[x] == -1:
                    q_values[x] = -20

            self.q_tables[entry] = q_values
            self.q_values[entry] = 0.6

        return q_values

    def update(self, game_status):
        last_action = True
        # If Player win
        if game_status == 1:
            self.set_q_value(1)
        elif game_status == -1:
            self.set_q_value(-1)
        else:
            self.set_q_value(3)

    def save_q_table(self, data_type_name):
        with open('q_table_' + str(self.mark) + '_' + data_type_name + '.pickle', 'wb') as f:
            pickle.dump(self.q_tables, f)

        with open('q_values_' + str(self.mark) + '_' + data_type_name + '.pickle', 'wb') as f:
            pickle.dump(self.q_values, f)

    # Load file with Q-Table
    def load_q_table(self, file_name):
        if self.check_if_file_exist(file_name):
            with open(file_name, 'rb') as f:
                try:
                    while True:
                        self.q_tables.update(pickle.load(f))
                except EOFError:
                    pass
        else:
            print("Players " + str(self.mark) + " Q-Table file '" + file_name + "' do not exist.")

    # Load file with Q-Values
    def load_q_values(self, file_name):
        if self.check_if_file_exist(file_name):
            with open(file_name, 'rb') as f:
                try:
                    while True:
                        self.q_values.update(pickle.load(f))
                except EOFError:
                    pass
        else:
            print("Players " + str(self.mark) + " Q-Values file '" + file_name + "' do not exist.")

    def export_q_table(self, name):

        file_name = 'q_table_' + str(self.mark) + '_' + name +'.txt'
        with open(file_name, 'w') as f:
            for key, value in self.q_tables.items():
                f.writelines(str(np.frombuffer(key, dtype='float64')).replace('[', "").replace(']', "") + ', ' + str(np.round(value, 4)).replace('[', "").replace(']', "") + '\n')

        file_name_1 = 'q_values_' + str(self.mark) + '_' + name + '.txt'
        with open(file_name_1, 'w') as f:
            for key, value in self.q_values.items():
                f.writelines(str(np.frombuffer(key, dtype='float64')).replace('[', "").replace(']', "") + ', ' + str(
                    np.round(value, 4)).replace('[', "").replace(']', "") + '\n')

    # File existence checker
    def check_if_file_exist(self, file_name):
        return os.path.isfile(file_name)

    # Pickle object serialization
    def save(self):
        pass
