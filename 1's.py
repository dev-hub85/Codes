import random

# Initialize parameters
L = 10  # Length of bit string
POPULATION_SIZE = 10
GENERATIONS = 50

# Function to generate random bit strings
def generate_individual():
    individual_population = []
    for i in range(L):
        individual_population.append(random.choice([0, 1]))
    return individual_population

# Fitness function to count the number of 1s
def fitness(individual):
    return sum(individual)

# Select two parents based on fitness
def select_parents(population):
    population = sorted(population, key=fitness, reverse=True)
    return population[0], population[1]

# Crossover: mix two parents
def crossover(parent1, parent2):
    point = random.randint(1, L-1)
    child = parent1[:point] + parent2[point:]
    return child

# Mutation: randomly flip a bit
def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

# Genetic algorithm
def genetic_algorithm():
    population = []
    for i in range(POPULATION_SIZE):
        population.append(generate_individual())

    for generation in range(GENERATIONS):
        print(f"Generation {generation}: Best fitness = {fitness(max(population, key=fitness))}")
        
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select_parents(population)
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            new_population.extend([child1, child2])
        
        population = new_population

        if fitness(max(population, key=fitness)) == L:
            print(f"Solution found in generation {generation}")
            break

    print("Best solution:", max(population, key=fitness))

genetic_algorithm()