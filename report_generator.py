import matplotlib.pyplot as plt
import numpy as np


def export_data(filename, game_total_count, wins_counter, lost_counter, ties_counter):
    with open(filename + '.txt', 'w') as f:
        f.write("Game count: " + str(game_total_count))
        f.write("Player QRL wins: " + str(wins_counter))
        f.write("Player QRL lost: " + str(lost_counter))
        f.write("Ties: " + str(ties_counter))


def calculate_score(data_list):
    counter_list = []
    wins_list = []
    lost_list = []
    ties_list = []
    counter, wins_counter, lost_counter, ties_counter = 0, 0, 0, 0

    # Separating (into three categories: wins, lost and ties) and counting input data
    for data in data_list:
        if data == 1:
            wins_list.append((counter, wins_counter))
            wins_counter = wins_counter + 1
        else:
            wins_list.append((counter, wins_counter))

        if data == 2:
            lost_list.append((counter, lost_counter))
            lost_counter = lost_counter + 1
        else:
            lost_list.append((counter, lost_counter))

        if data == 3:
            ties_list.append((counter, ties_counter))
            ties_counter = ties_counter + 1
        else:
            ties_list.append((counter, ties_counter))

        counter_list.append(counter)
        counter = counter + 1

    print("P1 wins:")
    print(wins_counter)
    print("P2 wins:")
    print(lost_counter)
    print("ties")
    print(ties_counter)


def plot_labels(data_list, filename, game_total_count):
    counter_list = []
    wins_list = []
    lost_list = []
    ties_list = []
    counter, wins_counter, lost_counter, ties_counter = 0, 0, 0, 0

    # Separating (into three categories: wins, lost and ties) and counting input data
    for data in data_list:
        if data == 1:
            wins_list.append((counter, wins_counter))
            wins_counter = wins_counter + 1
        else:
            wins_list.append((counter, wins_counter))

        if data == -1:
            lost_list.append((counter, lost_counter))
            lost_counter = lost_counter + 1
        else:
            lost_list.append((counter, lost_counter))

        if data == 3:
            ties_list.append((counter, ties_counter))
            ties_counter = ties_counter + 1
        else:
            ties_list.append((counter, ties_counter))

        counter_list.append(counter)
        counter = counter + 1

    print("P1 wins:")
    print(wins_counter)
    print("P2 wins:")
    print(lost_counter)
    print("ties")
    print(ties_counter)

    # Data converting to matplotlib.plot format
    wins_list_modified = [(elem_1 + 1, elem_2 / (elem_1 + 1)) for elem_1, elem_2 in wins_list]
    lost_list_modified = [(elem_1 + 1, elem_2 / (elem_1 + 1)) for elem_1, elem_2 in lost_list]
    ties_list_modified = [(elem_1 + 1, elem_2 / (elem_1 + 1)) for elem_1, elem_2 in ties_list]

    # Graph 1 creation
    plt.plot(*zip(*wins_list_modified), label='Player 1 Wins')
    plt.plot(*zip(*lost_list_modified), label='Player -1 Wins')
    plt.plot(*zip(*ties_list_modified), label='Ties')
    plt.legend()
    plt.title('Games statistics\nIterations: {}\nP1 wins: {}\nP2 wins: {}\nTies: {}'.format(len(data_list), wins_counter, lost_counter, ties_counter))
    plt.xlabel('Game number (Iteration) [-]')
    plt.xlim(left=1)
    plt.ylabel('Normalized Count [%]')
    plt.ylim(bottom=0)
    plt.draw()
    plt.savefig(filename + '_1.png', dpi=200)
    plt.show()

    # Data converting to matplotlib.plot format
    wins_list_modified = [(elem_1 + 1, elem_2 + 1) for elem_1, elem_2 in wins_list]
    lost_list_modified = [(elem_1 + 1, elem_2 + 1) for elem_1, elem_2 in lost_list]
    ties_list_modified = [(elem_1 + 1, elem_2 + 1) for elem_1, elem_2 in ties_list]

    # Graph 2 creation
    plt.plot(*zip(*wins_list_modified), label='Player 1 Wins')
    plt.plot(*zip(*lost_list_modified), label='Player -1 Wins')
    plt.plot(*zip(*ties_list_modified), label='Ties')
    plt.legend()
    plt.title(
        'Games statistics\nIterations: {}\nP1 wins: {}\nP2 wins: {}\nTies: {}'.format(len(data_list), wins_counter,
                                                                                      lost_counter, ties_counter))
    plt.xlabel('Game number (Iteration) [-]')
    plt.xlim(left=1)
    plt.ylabel('Count [-]')
    plt.ylim(bottom=1)
    plt.draw()
    plt.savefig(filename + '_2.png', dpi=200)
    plt.show()

    # Export obtain score
    export_data(filename, game_total_count, wins_counter, lost_counter, ties_counter)
