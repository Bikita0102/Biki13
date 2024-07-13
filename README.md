
## Installation
1.  Clone the repository:
```bash
git clone https://github.com/Bikita0102/Biki13
```
## Usage
To run the genetic algorithm, execute the main script geneticalgo.ipynb. Ensure Python 3.x is installed on your system.

## Parameters
- population_size: Size of the population.
- mutation_rate: Mutation rate, probability of a bit mutating.
- generations: Number of generations.
- int_length: Length of the binary encoding for the integer part of the solution.
- frac_length: Length of the binary encoding for the fractional part of the solution.

## Fitness Function
The fitness function used in this implementation is defined as:
```bash
def fitness_function(x):
    return abs(3 * x**2 - 7 * x + 2)
```
## Encoding and Decoding
### Encoding:
Each individual in the population is represented as a binary string, where:
- The first length_integer bits represent the integer part.
- The next length_fraction bits represent the fractional part.
Use the encode and decode functions to convert between binary strings and decimal values.

## Initial Population
The initial population is generated randomly within a specified range [-128, 128] using the init_population function.

## Selection
Roulette wheel selection (roulette_wheel_selection function) is employed to select individuals based on their fitness values for reproduction.

## Crossover
single crossover (single_point_crossover function) is used to combine genetic material from selected parents to produce offspring.

## Mutation
Mutation (mutate function) introduces random changes in offspring to maintain genetic diversity and explore new solutions.

## Genetic Algorithm Execution
The genetic algorithm (genetic_algorithm function) orchestrates the iterative process of selection, crossover, mutation, and fitness evaluation over multiple generations to find the optimal solution.

## Example Usage
```bash
# Example usage
from genetic_algorithm import genetic_algorithm, decode, fitness_function

# Parameters
population_size = 10
mutation_rate = 0.05
generations = 10
int_length = 8
frac_length = 6
total_length = int_length + frac_length

# Initial population
init_population = [encode(random.uniform(-128, 128)) for _ in range(population_size)]

# Execute genetic algorithm
best_solution = genetic_algorithm(init_population)
decoded_solution = decode(best_solution)
print(f"Best solution found: x = {decoded_solution}, Fitness = {fitness_function(decoded_solution)}")
```

```bash
Best solution found: x = 179.46875, Root/Fitness = 95372.8154296875
```
