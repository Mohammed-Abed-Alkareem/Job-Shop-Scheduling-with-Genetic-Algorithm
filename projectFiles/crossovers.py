import random


def modified_order_crossover(parent1, parent2):
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

    def correct_job_order(child):
        jobs = set(phase.job for phase in child)
        for job in jobs:
            phases = [phase for phase in child if phase.job == job]
            phases.sort(key=lambda phase: phase.phase_order)
            for i, phase in enumerate(phases):
                index = child.index(phase)
                # Swap if the current phase is out of order
                if index != i:
                    child[index], child[i] = child[i], child[index]

    correct_job_order(child1)
    correct_job_order(child2)

    return tuple(child1), tuple(child2)


def make_crossover(parent1, parent2):
    child1 = []
    child2 = []

    # Get the length of the chromosome
    chromosome_length = len(parent1)
    #get two random number less than the length of the chromosome TO MAKE THE CUTT
    cut1 = random.randint(1, chromosome_length - 3)
    cut2 = random.randint(cut1+1, chromosome_length - 2)



    # print('length of chromosome: ', chromosome_length)
    #
    # print("Cut1: ", cut1)
    # print("Cut2: ", cut2)

    #then fill the rest in between cut 1 and cut 2 from parent2 to child1 if not in child 1
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

    return tuple(child1), tuple(child2)
