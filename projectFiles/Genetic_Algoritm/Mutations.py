import random
random.seed()


def make_mutation(chromosome):

    chromosome = list(chromosome)
    while True:
        # Get two phases to swap
        phase1 = random.choice(chromosome)
        phase2 = random.choice(chromosome)
        while phase1 == phase2:
            phase2 = random.choice(chromosome)  # Ensure phase1 and phase2 are different

        # Find the indices of the two phases
        index1 = chromosome.index(phase1)
        index2 = chromosome.index(phase2)

        # Swap the two phases
        chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]

        # Check if the phase does not have any phase from the same job that's order is less than it before it
        invalid_chromosome = False
        for i in range(1, len(chromosome)):
            if chromosome[i].job == chromosome[i-1].job and chromosome[i].phase_order < chromosome[i-1].phase_order:
                invalid_chromosome = True
                break

        if not invalid_chromosome:
            break

    return tuple(chromosome)