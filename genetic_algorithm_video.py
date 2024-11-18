import random

# Target string
target = "tacocat"
length = 7

# Initalizing important variables 
population_size = 100
maximum_generations = 1000
mutation_rate = 0.01
crossover_rate = 0.7 

# generates a random string that is the same length as the target from a given list of characters
def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

# fitness is based on how many of the same characters an individual has when compared to the target
def fitness(individual):
    return sum(1 for i, char in enumerate(individual) if char == target[i])

# select function: chooses top half of the population based on fitness
def select(population):
    # Sort population by fitness in descending order and pick the top half
    population.sort(key=lambda x: fitness(x), reverse=True)
    return population[:population_size // 2]

# crossover function: combines two fit parents to create two offspring
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        # Choose a random crossover point
        point = random.randint(1, len(parent1) - 1)
        # Create two offspring
        offspring1 = parent1[:point] + parent2[point:]
        offspring2 = parent2[:point] + parent1[point:]
        return offspring1, offspring2
    else:
        return parent1, parent2

# mutation function: occasionally mutate an individual by changing one character randomly to maintain genetic diversity 
def mutate(individual):
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        individual = individual[:index] + new_char + individual[index+1:]
    return individual

# Main Algorithm function
def genetic_algorithm():
    # Initialize population with random strings
    population = [random_string(len(target)) for _ in range(population_size)]

    for generation in range(maximum_generations):
        # fitness evaluation and selection of top half of population 
        population = select(population)

        # creation of next generation through crossover and mutation
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.choices(population, k=2)
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation.append(mutate(offspring1))
            next_generation.append(mutate(offspring2))

        # Replace the old generation with the new one
        population = next_generation

        # Check if the target string has been found 
        for individual in population:
            if individual == target:
                print(f"The target string '{target}' has been found in generation {generation}! ")
                return individual

    print("Target string was unable to be found in the given number of generations.")
    return None

# Run the algorithm
result = genetic_algorithm()

if result:
    print(f"Target string: {result} has been found")
else:
    print("{target} has not been found ")
