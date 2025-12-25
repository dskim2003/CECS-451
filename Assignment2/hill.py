import board
import time
import random

start_time = time.time()

def findLowestValue(states):
    min_index = 0
    for state in states:
        if state.get_fitness() < states[min_index].get_fitness():
            min_index = states.index(state)
    return min_index

def generateNeighboringStates(board):
    states = []
    for i in range(5):
        new_board = board
        if (random.randint(0,1) == 0):
            col = new_board.get_map()[i].index(1)
            new_board.flip(i, col)
            col -= 1
            if (col < 0):
                col = 4
            new_board.flip(i, col)
        else:
            col = new_board.get_map()[i].index(1)
            new_board.flip(i, col)
            col += 1
            if (col > 4):
                col = 0
            new_board.flip(i, col)
        states.append(new_board)
    return states



current_board = board.Board(5)

while (current_board.get_fitness() != 0):
    states = generateNeighboringStates(current_board)

    if (states[findLowestValue(states)].get_fitness() < current_board.get_fitness()):
        current_board = states[findLowestValue(states)]
        current_board.print_map()
    elif (states[findLowestValue(states)].get_fitness() == current_board.get_fitness()):
        current_board = board.Board(5)



end_time = time.time() - start_time
print("Running time: " + str(end_time * 1000) + "ms")
current_board.print_map()
