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


def cross_over(parent1, parent2):
    '''this is another crossover by taking phase from one parent and the other from the other parent and so on make sure that the phase doesnot already exists in the child'''
    child1 = []
    child2 = []
    P1 = 0
    P2 = 0

    # print("parent 1")
    # for phase in parent1:
    #     print(phase)
    #
    #
    # print("parent 2")
    # for phase in parent2:
    #     print(phase)


    #if the phase is already in the child go to next phase
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

    # print("child 1")
    # for phase in child1:
    #     print(phase)

    # print(check_order(child1))

    # print("child 2")
    # for phase in child2:
    #     print(phase)

    # print(check_order(child2))

    while not check_order(child1):
        print("Correcting child 1")
        child1 = correct_job_order(child1)

    while not check_order(child2):
        print("Correcting child 2")
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
    jobs = {}
    swap_made = True  # Initialize swap_made to True to enter the while loop

    print("Correcting job order")

    while swap_made:  # Continue until no swaps are made in a full pass
        swap_made = False  # Reset swap_made to False at the start of each pass
        jobs = {}
        for phase in chromosome:
            if phase.job in jobs:
                if jobs[phase.job] > phase.phase_order:
                    print("Swapping")
                    # Find the phase that is in its order and swap it with the current phase
                    for i in range(chromosome.index(phase) - 1):
                        if chromosome[i].job == phase.job and chromosome[i].phase_order > phase.phase_order:
                            print(f"Swapping {chromosome[i]} with {chromosome[chromosome.index(phase)]}")

                            chromosome[i], chromosome[chromosome.index(phase)] = (
                                chromosome[chromosome.index(phase)], chromosome[i])

                            swap_made = True  # Set swap_made to True because a swap was made
                            break  # Break the inner loop to restart from the first phase
                jobs[phase.job] = phase.phase_order  # Update the phase order in the dictionary
            else:
                jobs[phase.job] = phase.phase_order  # Initialize the phase order in the dictionary

    return tuple(chromosome)
