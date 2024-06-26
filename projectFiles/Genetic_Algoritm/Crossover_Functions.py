import random
random.seed()


# Partially mapped crossover, works by selecting two crossover points and swapping the segments between these points.
# It preserves the order and position of as many genes as possible from the parents.
# Mapping relationships are created to ensure that each gene appears exactly once in the offspring.
def partially_mapped_crossover(parent1, parent2):
    chromosome_length = len(parent1)
    start_cut = random.randint(0, chromosome_length - 1)
    end_cut = random.randint(start_cut + 1, chromosome_length)

    def get_child(p1, p2):
        child = [None] * chromosome_length

        child[start_cut:end_cut] = p1[start_cut:end_cut]

        mapping = {p1[i]: p2[i] for i in range(start_cut, end_cut)}

        for i in range(chromosome_length):
            if child[i] is None:
                item = p2[i]
                while item in child:
                    item = mapping.get(item, item)
                child[i] = item

        return child

    child1 = get_child(parent1, parent2)
    child2 = get_child(parent2, parent1)

    def correct_job_order(child):
        jobs = set(phase.job for phase in child)
        for job in jobs:
            phases = [phase for phase in child if phase.job == job]
            phases.sort(key=lambda phase: phase.phase_order)
            p = 0
            for index, phase in enumerate(child):
                if phase.job == job:
                    child[index] = phases[p]
                    p += 1

    correct_job_order(child1)
    correct_job_order(child2)

    return tuple(child1), tuple(child2)


# A single segment (subsequence) is selected from one parent and directly copied to the offspring.
# The remaining genes are filled in from the second parent while preserving their order,
# excluding those already present in the segment copied from the first parent.
def single_segment_crossover(parent1, parent2):
    child1 = []
    child2 = []
    parent1 = list(parent1)
    parent2 = list(parent2)

    chromosome_length = len(parent1)
    split_position = random.randint(1, chromosome_length - 1)

    # Splitting parents into left and right segments
    parent1_left_split, parent1_right_split = parent1[:split_position], parent1[split_position:]
    parent2_left_split, parent2_right_split = parent2[:split_position], parent2[split_position:]

    # Initialize children with the right segments copied
    child1 = parent1_right_split.copy()
    child2 = parent2_right_split.copy()

    # To maintain set for checking duplicates efficiently
    child1_elements = set(child1)
    child2_elements = set(child2)

    # Filling left side
    for item in reversed(parent2_left_split):
        if item not in child1_elements:
            child1.insert(0, item)
            child1_elements.add(item)

    # Ensure that we fill child2 with elements from parent1's left split if they are not duplicates
    for item in reversed(parent1_left_split):
        if item not in child2_elements:
            child2.insert(0, item)
            child2_elements.add(item)

    # Replace missing elements, ensuring every element from parents is included once
    for item in parent1:
        if item not in child1_elements:
            child1.append(item)
            child1_elements.add(item)

    for item in parent2:
        if item not in child2_elements:
            child2.append(item)
            child2_elements.add(item)

    while not check_order(child1):
        child1 = correct_job_order(child1)

    while not check_order(child2):
        child2 = correct_job_order(child2)

    return tuple(child1), tuple(child2)


# Double Segment Crossover involves selecting two segments from one parent and copying them directly to the offspring.
# The genes outside these segments are filled in from the second parent,
# maintaining their order and excluding any genes already present in the copied segments.
def double_segment_crossover(parent1, parent2):
    child1 = []
    child2 = []

    chromosome_length = len(parent1)
    # get two random number less than the length of the chromosome TO MAKE THE CUTT
    cut1 = random.randint(1, chromosome_length - 3)
    cut2 = random.randint(cut1+1, chromosome_length - 2)

    # then fill the rest in between cut 1 and cut 2 from parent2 to child1 if not in child 1
    child1 = list(parent1[:cut1] + parent1[cut2:])
    for phase in parent2:
        if phase not in child1:
            # append after cut1 and before cut2
            child1.insert(cut1, phase)
            cut1 += 1

    child2 = list(parent2[:cut1] + parent2[cut2:])
    for phase in parent1:
        if phase not in child2:
            child2.insert(cut1, phase)
            cut1 += 1

    while not check_order(child1):
        child1 = correct_job_order(child1)

    while not check_order(child2):
        child2 = correct_job_order(child2)

    return tuple(child1), tuple(child2)


# Alternating Parental Crossover constructs the offspring by alternately taking genes from each parent.
# Starting with one parent, the first gene is taken, then the second gene from the other parent,
# and so on, ensuring that the order of genes is maintained and each gene appears only once in the offspring.
def alternating_parental_gene_crossover(parent1, parent2):
    '''this is another crossover by taking phase from one parent and the other from the other parent and so on make sure that the phase doesnot already exists in the child'''
    child1 = []
    child2 = []
    P1 = 0
    P2 = 0

    while len(child1) < len(parent1):
        if len(child1) % 2 == 0:
            if parent1[P1] not in child1:
                child1.append(parent1[P1])
            else:
                P1 += 1

        else:
            if parent2[P2] not in child1:
                child1.append(parent2[P2])
            else:
                P2 += 1

    P1 = 0
    P2 = 0
    while len(child2) < len(parent2):
        if len(child2) % 2 == 1:
            if parent1[P1] not in child2:
                child2.append(parent1[P1])
            else:
                P1 += 1
        else:
            if parent2[P2] not in child2:
                child2.append(parent2[P2])
            else:
                P2 += 1

    while not check_order(child1):
        child1 = correct_job_order(child1)

    while not check_order(child2):
        child2 = correct_job_order(child2)

    return tuple(child1), tuple(child2)


def check_order(chromosome):
    jobs = {}
    for phase in chromosome:
        if phase.job in jobs:

            if jobs[phase.job] > phase.phase_order:
                return False

            jobs[phase.job] = phase.phase_order

        else:
            jobs[phase.job] = 1

    return True


def correct_job_order(chromosome):

    chromosome = list(chromosome)

    job_phases = {}
    job_indecies = {}
    for phase in chromosome:
        job = phase.job
        if job not in job_indecies:
            job_indecies[job] = []
            job_phases[job] = []
        job_phases[job].append(phase)
        job_indecies[job].append(chromosome.index(phase))

    # sort each list in job phases based on order
    for job in job_phases:
        job_phases[job] = sorted(job_phases[job], key=lambda x: x.phase_order)

    for job in job_indecies:
        for index in job_indecies[job]:
            # aapend at the correct index
            chromosome[index] = job_phases[job].pop(0)

    return tuple(chromosome)
