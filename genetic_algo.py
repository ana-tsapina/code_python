import random
import string

# Parameters
TARGET = "unitCircle"
POP_SIZE = 100  # Population size
MUTATION_RATE = 0.01  # Mutation probability
GEN_MAX = 1000  # Maximum generations

# Helper function to generate a random string
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Fitness function: Returns how many characters match the target string
def fitness(individual):
    return sum(1 for i, char in enumerate(individual) if char == TARGET[i])

# Crossover function: Combines two individuals to create a new one
def crossover(parent1, parent2):
    # Randomly choose a crossover point
    point = random.randint(1, len(TARGET) - 1)
    child = parent1[:point] + parent2[point:]
    return child

# Mutation function: Randomly mutate an individual with a given mutation rate
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(string.ascii_letters)
    return ''.join(individual)

# Main Genetic Algorithm function
def genetic_algorithm():
    # Initialize population
    population = [random_string(len(TARGET)) for _ in range(POP_SIZE)]
    
    for generation in range(GEN_MAX):
        # Sort population by fitness (higher fitness is better)
        population.sort(key=lambda x: fitness(x), reverse=True)
        
        # Check if we found the target string
        if fitness(population[0]) == len(TARGET):
            print(f"Target '{TARGET}' found in generation {generation}")
            return population[0]

        # Create new population (selection, crossover, mutation)
        new_population = []
        
        # Elitism: Carry over the top half of the population
        new_population.extend(population[:POP_SIZE // 2])
        
        # Fill the remaining population with offspring
        while len(new_population) < POP_SIZE:
            parent1, parent2 = random.choices(population[:POP_SIZE // 2], k=2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        # Replace old population with new population
        population = new_population
    
    print("Reached maximum generations without finding target.")
    return population[0]

# Run the genetic algorithm
best_individual = genetic_algorithm()
print(f"Best individual: {best_individual}")
