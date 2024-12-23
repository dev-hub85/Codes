import random

# Items for the knapsack problem
items = [[1, 2], [2, 4], [3, 4], [4, 5], [5, 7], [6, 9]]
max_weight = 10
population_size = 10
mutation_probability = 0.2
generations = 10

# Generate a random population
def generate_population(size):
    return [[random.choice([0, 1]) for _ in range(len(items))] for _ in range(size)]

# Calculate fitness of a chromosome
def calculate_fitness(chromosome):
    total_weight = sum(items[i][0] for i in range(len(chromosome)) if chromosome[i] == 1)
    total_value = sum(items[i][1] for i in range(len(chromosome)) if chromosome[i] == 1)
    return total_value if total_weight <= max_weight else 0

# Select two chromosomes based on fitness
def select_chromosomes(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_values)
    if total_fitness == 0: return random.sample(population, 2)
    fitness_values = [f / total_fitness for f in fitness_values]
    return random.choices(population, weights=fitness_values, k=2)

# Perform crossover between two chromosomes
def crossover(parent1, parent2):
    point = random.randint(0, len(items) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Perform mutation on a chromosome
def mutate(chromosome):
    point = random.randint(0, len(items) - 1)
    chromosome[point] = 1 - chromosome[point]
    return chromosome

# Get the best chromosome in the population
def get_best(population):
    return max(population, key=calculate_fitness)

# Print available items
print("Available items:", items)

# Generate initial population
population = generate_population(population_size)

# Evolve population for the given number of generations
for _ in range(generations):
    parent1, parent2 = select_chromosomes(population)
    child1, child2 = crossover(parent1, parent2)

    if random.random() < mutation_probability: child1 = mutate(child1)
    if random.random() < mutation_probability: child2 = mutate(child2)

    population = [child1, child2] + population[2:]

# Find the best solution
best = get_best(population)

# Calculate and print the result
total_weight = sum(items[i][0] for i in range(len(best)) if best[i] == 1)
total_value = sum(items[i][1] for i in range(len(best)) if best[i] == 1)

print("\nThe best solution:")
print("Weight:", total_weight)
print("Value:", total_value)
