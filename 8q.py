import random

BOARD_SIZE = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 10000

def fitness(individual):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return -conflicts

def create_individual():
    individual = []  # To store the queen positions on the board
    for _ in range(BOARD_SIZE):
        individual.append(random.randint(0, BOARD_SIZE - 1))
    return individual

def crossover(parent1, parent2):
    point = random.randint(0, BOARD_SIZE - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual[random.randint(0, BOARD_SIZE - 1)] = random.randint(0, BOARD_SIZE - 1)

def print_board(individual):
    for row in range(BOARD_SIZE):
        line = ["Q" if col == individual[row] else "." for col in range(BOARD_SIZE)]
        print(" ".join(line))

def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    for _ in range(MAX_GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == 0:
            return population[0]

        next_generation = population[:POPULATION_SIZE // 2]
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(next_generation, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)

        population = next_generation

    return None

if __name__ == "__main__":
    solution = genetic_algorithm()
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found.")