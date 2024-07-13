import random
import math

# Parameters
population_size = 10
mutation_rate = 0.05
generations = 10
int_length = 8
frac_length = 6
total_length = int_length + frac_length

# Fitness Function
def fitness_function(x):
    return abs(3 * x**2 - 7 * x + 2)

# Binary Encoding
def encode(x):
    integer_part = int(x)
    fractional_part = abs(x - integer_part)
    integer_bin = format(integer_part & ((1 << int_length) - 1), f'0{int_length}b')
    fractional_bin = ''.join(str(int(fractional_part * 2**i) % 2) for i in range(1, frac_length + 1))
    return integer_bin + fractional_bin

def decode(b):
    integer_part = int(b[:int_length], 2)
    fractional_part = sum(int(bit) * 2**-i for i, bit in enumerate(b[int_length:], 1))
    return integer_part + fractional_part

# Initial Population
init_population = [encode(random.uniform(-128, 128)) for _ in range(population_size)]

# Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    pointer = random.random()
    cumulative_prob = 0
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if pointer <= cumulative_prob:
            return population[i]

# Single-point Crossover
def single_point_crossover(parent1, parent2):
    point = random.randint(1, total_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)

# Genetic Algorithm
def genetic_algorithm(init_population):
    population = init_population

    for generation in range(generations):
        fitness_values = [fitness_function(decode(x)) for x in population]

        parent1 = roulette_wheel_selection(population, fitness_values)
        parent2 = roulette_wheel_selection(population, fitness_values)

        child1, child2 = single_point_crossover(parent1, parent2)

        child1 = mutate(child1)
        child2 = mutate(child2)

        population.sort(key=lambda x: fitness_function(decode(x)), reverse=True)
        population[-2] = child1
        population[-1] = child2

    best_individual = min(population, key=lambda x: fitness_function(decode(x)))
    return best_individual

best_solution = genetic_algorithm(init_population)
decoded_solution = decode(best_solution)
print(f"Best solution found: x = {decoded_solution}, Root/Fitness = {fitness_function(decoded_solution)}")
