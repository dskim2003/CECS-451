import board
import random
import time

def selection(states):
    states.sort(key=lambda x: x.get_fitness(), reverse=True)
    denominator = 0
    for state in states:
        denominator += state.get_fitness()

    probabilities = []
    for state in states:
        probabilities.append(state.get_fitness() / denominator)

    loop = True
    total = 0
    temp = 0
    r = random.random()
    while (loop):
        if (temp == len(states) - 1):
            selection_index = len(states) - 1
            loop = False
        total = total + probabilities[temp]
        if (r < total):
            selection_index = temp
            loop = False
        temp += 1
    return selection_index

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 4)

    substr1 = parent1.encode()[:crossover_point] + parent2.encode()[crossover_point:]
    substr2 = parent2.encode()[:crossover_point] + parent1.encode()[crossover_point:]


    child1 = board.Board(5)
    child2 = board.Board(5)

    child1.decode(substr1)
    child2.decode(substr2)


    return child1, child2

def mutate(state):
    mutation_point = random.randint(0, 4)
    mutation_value = random.randint(0, 4)

    code = state.encode()

    newcode = code[:mutation_point] + str(mutation_value) + code[mutation_point + 1:]

    newboard = board.Board(5)
    newboard.decode(newcode)

    return newboard


start_time = time.time()

states = []
for i in range(8):
    states.append(board.Board(5))

is_complete = False

while (not is_complete):
    states.sort(key=lambda x: x.get_fitness())
    if (states[0].get_fitness() == 0):
        is_complete = True
        break
    index = selection(states)
    new_list = []

    for state in states:
        if (len(new_list) >= 8):
            break
        if (state != states[index]):
            child1, child2 = crossover(states[index], state)
            new_list.append(child1)
            new_list.append(child2)


    for i in range(len(new_list)):
        new_list[i] = mutate(new_list[i])        


    states = new_list

    
end_time = time.time() - start_time
print("Running time: " + str(end_time * 1000) + "ms")
states[0].print_map()