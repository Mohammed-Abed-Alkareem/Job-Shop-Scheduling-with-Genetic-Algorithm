import random
random.seed()


def correct_job_order(chromosome):
    jobs = set(phase.job for phase in chromosome)
    for job in jobs:
        phases = [phase for phase in chromosome if phase.job == job]
        phases.sort(key=lambda phase: phase.phase_order)
        p = 0
        for index, phase in enumerate(chromosome):
            if phase.job == job:
                chromosome[index] = phases[p]
                p += 1


# Choosing two positions and swapping them
def swapping_mutation(chromosome):

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


# Choosing a segment and sorting it in reverse
def inversion_mutation(chromosome):
    chromosome = list(chromosome)
    size = len(chromosome) // 3
    mutated_chromosome = chromosome.copy()

    start = random.randint(0, len(chromosome) - size - 1)
    end = start + size

    subset = mutated_chromosome[start:end + 1]
    subset.reverse()
    mutated_chromosome[start:end + 1] = subset

    correct_job_order(mutated_chromosome)

    return tuple(mutated_chromosome)


# Choosing a segment and randomly shuffling it
def scramble_mutation(chromosome):
    chromosome = list(chromosome)
    size = len(chromosome) // 3
    mutated_chromosome = chromosome.copy()

    start = random.randint(0, len(chromosome) - size - 1)
    end = start + size

    subset = mutated_chromosome[start:end + 1]
    random.shuffle(subset)
    mutated_chromosome[start:end + 1] = subset

    correct_job_order(mutated_chromosome)

    return tuple(mutated_chromosome)
