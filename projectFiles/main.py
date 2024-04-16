import random
import time

from read_csv import dictionary_store

Jobs = dictionary_store("job_shop_schedule.csv")
random.seed(time.time())

import copy



def create_chromosome(Jobs , population_size = 20):

    population = set()
    x = 0

    while len(population) < population_size:
        x += 1 # count the number of iterations
        chromosome = []
        Jobs_copy = copy.deepcopy(Jobs)  # Create a copy of Jobs
        while Jobs_copy:
            job = random.choice(list(Jobs_copy.keys()))
            if Jobs_copy[job]:
                phase = Jobs_copy[job].pop(0)
                chromosome.append((job, phase))
            else:
                del Jobs_copy[job]

        # Convert the chromosome to a tuple before adding to the set
        population.add(tuple(chromosome))

    # Convert the set back to a list for consistency with the rest of your code
    population = list(population)

    print("Population")
    for chromosome in population:
        print(chromosome)

    print(x)
    return population


print(len(create_chromosome(Jobs)))