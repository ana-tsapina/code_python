import random

# Target string
TARGET = "tacocat"

# Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
MAX_GENERATIONS = 1000
CROSSOVER_RATE = 0.7

# Function to generate a random string of the same length as TARGET
def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

# Fitness function to calculate how many characters in the individual match the target string
def fitness(individual):
    return sum(1 for i, char in enumerate(individual) if char == TARGET[i])

# Selection function: Select individuals based on their fitness
def select(population):
    # Sort population by fitness in descending order and pick the top half
    population.sort(key=lambda x: fitness(x), reverse=True)
    return population[:POPULATION_SIZE // 2]

# Crossover function: Combine two parents to create two offspring
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        # Choose a random crossover point
        point = random.randint(1, len(parent1) - 1)
        # Create two offspring
        offspring1 = parent1[:point] + parent2[point:]
        offspring2 = parent2[:point] + parent1[point:]
        return offspring1, offspring2
    else:
        return parent1, parent2

# Mutation function: Mutate an individual by changing one character randomly
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        individual = individual[:index] + new_char + individual[index+1:]
    return individual

# Main Genetic Algorithm function
def genetic_algorithm():
    # Initialize population with random strings
    population = [random_string(len(TARGET)) for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Evaluate fitness and select the top half of the population
        population = select(population)

        # Generate new population through crossover and mutation
        new_generation = []
        while len(new_generation) < POPULATION_SIZE:
            parent1, parent2 = random.choices(population, k=2)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_generation.append(mutate(offspring1))
            new_generation.append(mutate(offspring2))

        # Replace the old population with the new one
        population = new_generation

        # Check if the target string is found
        for individual in population:
            if individual == TARGET:
                print(f"Target string '{TARGET}' found in generation {generation}")
                return individual

    print("Target string not found within the given number of generations.")
    return None

# Run the genetic algorithm
result = genetic_algorithm()

if result:
    print(f"Found target string: {result}")
else:
    print("Failed to find the target string.")
