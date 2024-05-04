import copy


import random

from projectFiles.Genetic_Algoritm.Fitness_Functions import get_makespan
from projectFiles.Data.read_csv import dictionary_store

random.seed()

import matplotlib.pyplot as plt

from matplotlib.patches import Patch

from projectFiles.Genetic_Algoritm.Job_Phases import *
from projectFiles.Genetic_Algoritm.Crossover_Functions import make_crossover


def create_chromosome(Jobs, population_size = 8):

    population = []
    x = 0

    while len(population) < population_size:

        x += 1 # count the number of iterations

        chromosome = []
        Jobs_copy = copy.deepcopy(Jobs)  # Create a copy of Jobs

        job_phase_order = {}

        for job in Jobs.keys():
            job_phase_order[job] = 1

        while Jobs_copy:

            job = random.choice(list(Jobs_copy.keys()))
            if Jobs_copy[job]:
                phase = Jobs_copy[job].pop(0)
                # chromosome.append((job, phase))

                chromosome.append(
                    Phases(
                        job=job,
                        phase_order=job_phase_order[job],
                        machine=phase[0],
                        duration=phase[1]
                    )
                )

                job_phase_order[job] += 1
            else:
                del Jobs_copy[job]

        # Convert the chromosome to a tuple before adding to the set
        population.append(tuple(chromosome))

    # # Convert the set back to a list for consistency with the rest of your code
    # population = list(population)

    # print("Population")
    # for chromosome in population:
    #     # print(chromosome)
    #     # print(len(chromosome))
    #     print("_____________________________________________________")
    #     for phase in chromosome:
    #         print(phase.__repr__())
    #
    # print(x)
    return population


def machine_phases(chromosome):

    machines_process = {}  #the dictionary for machines phase order
    jobs = {}  # to store weather if a job is currently working

    for phase in chromosome:
        machines_process[phase.machine] = {'process': [], 'finish_time': 0, 'start_time': 0}
        jobs[phase.job] = {'available': True, 'order': 1, 'available_at': 0}


    #sort machines_process based on the number after M
    machines_process = dict(sorted(machines_process.items(), key=lambda x: int(x[0][1:])))

    # print(machines_process)

    jobs = dict(sorted(jobs.items()))

    chrom = list(chromosome)

    # print(chrom)

    t = 0
    while True:
        # print("Time: ", t)
        #print machines that are available
        # for mach in machines_process:
        #     print(mach, machines_process[mach])

        for phase in chromosome:

            if (jobs[phase.job]['available'] and
                    jobs[phase.job]['order'] == phase.phase_order and
                    machines_process[phase.machine]['finish_time'] <= t):

                # print("in the if statement")
                # print("Job: ", phase.job, "Machine: ", phase.machine, "Duration: ", phase.duration, "Start Time: ", t)
                jobs[phase.job]['available'] = False
                jobs[phase.job]['available_at'] = phase.duration + t - 1  # Adjust here

                machines_process[phase.machine]['finish_time'] = phase.duration + t

#                #store the start time of the machine only for first time
                if machines_process[phase.machine]['start_time'] == 0:
                    machines_process[phase.machine]['start_time'] = t

                machines_process[phase.machine]['process'].append(
                    ProcessPhases(job=phase.job,
                                  phase_order=jobs[phase.job]['order'],
                                  machine=phase.machine,
                                  duration=phase.duration,
                                  start_time=t
                                  )
                )

                jobs[phase.job]['order'] += 1

                chrom.remove(phase)

            # else:
            #     print("in the else statement")
            #     print("Job: ", phase.job, "Machine: ", phase.machine, "Duration: ", phase.duration, "Start Time: ", t)

        for phase in chrom:
            if jobs[phase.job]['available_at'] == t:
                # print("yes")
                jobs[phase.job]['available'] = True

        if not chrom:
            break

        t += 1

    # print("machines_process")
    # for machine in machines_process:
    #     print(machine, machines_process[machine])

    # print("jobs")
    # for job in jobs:
    #     print(job, jobs[job])

    return machines_process


def draw_gantt_chart(machines_process, jobs, ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 8))

    else:
        ax.clear()

    yticks = []
    yticklabels = []

    colors = plt.cm.tab20.colors

    job_colors = {job: colors[i % len(colors)] for i, job in enumerate(jobs)}

    for i, machine in enumerate(machines_process):
        yticks.append(i)
        yticklabels.append(machine)
        for phase in machines_process[machine]['process']:
            ax.broken_barh([(phase.start_time, phase.duration)], (i - 0.4, 0.8), facecolors=job_colors[phase.job])

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.set_xlabel("Time", fontsize=18)
    ax.set_ylabel("Machine", fontsize=18)
    ax.set_title("Gantt Chart", fontsize=22)


    # make the x axis more divided
    ax.set_xticks(range(0, max([phase.start_time + phase.duration for machine in machines_process for phase in machines_process[machine]['process']]), 10))



    legend_patches = [Patch(color=color, label=job) for job, color in job_colors.items()]

    # Adjust the legend box
    ax.legend(handles=legend_patches, bbox_to_anchor=(1, 1), loc='upper left', prop={'size': 12}, fancybox=True, shadow=True, edgecolor='black', facecolor='white', framealpha=0.7)

    #start from 0
    ax.set_xlim(0, max([phase.start_time + phase.duration for machine in machines_process for phase in machines_process[machine]['process']]))

    # Set the title and labels
    ax.set_title('Gantt Chart')
    ax.set_xlabel('Time')
    ax.set_ylabel('Machines')

    #plt.show()
    # Redraw the figure
    ax.figure.canvas.draw()


def extract_jobs(machines_process):
    jobs = set()
    for machine_data in machines_process.values():
        for process_phase in machine_data['process']:
            jobs.add(process_phase.job)

    #sort the set based on the number after _
    jobs = sorted(jobs, key=lambda x: int(x.split("_")[1]))

    return jobs


# def make_mutation(chromosome):
#     # Get two phases to swap
#     phase1 = random.choice(chromosome)
#     phase2 = random.choice(chromosome)
#     while phase1 == phase2:
#         phase2 = random.choice(chromosome)  # Ensure phase1 and phase2 are different
#
#     # Find the indices of the two phases
#     index1 = chromosome.index(phase1)
#     index2 = chromosome.index(phase2)
#
#     chromosome = list(chromosome)
#
#     for i in range(index2, len(chromosome)):
#         if chromosome[index1].job == chromosome[i].job and chromosome[index1].phase_order > chromosome[i].phase_order:
#             make_mutation(chromosome)
#             break
#
#     for i in range(index1, len(chromosome)):
#         if chromosome[index2].job == chromosome[i].job and chromosome[index2].phase_order > chromosome[i].phase_order:
#             make_mutation(chromosome)
#             break
#
#     # Swap the two phases
#     chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
#
#     #chek if the phase doesnot have any phase from the same jobe thats order is less than is before it
#     for i in range(1, len(chromosome)):
#         if chromosome[i].job == chromosome[i-1].job and chromosome[i].phase_order < chromosome[i-1].phase_order:
#             make_mutation(chromosome)  # Call the function again to swap two different phases
#             break
#
#     return tuple(chromosome)


def make_mutation(chromosome):
    # print("Mutation")
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


def get_weights(population, fitness_function=get_makespan):
    sum_fitness = 0
    weights = []

    for chromosome in population:
        fitness_value = fitness_function(machine_phases(chromosome))
        sum_fitness += 1 / fitness_value
        weights.append(1 / fitness_value)

    #devied the weights by the sum of the fitness
    weights = [weight / sum_fitness for weight in weights]

    #i checked that the sum is 1

    return weights


def generate_new_population(population, weights, population_size, mutation_rate=0.01, crossover_function=make_crossover):
    new_population = []

    while len(new_population) < population_size:
        parent1 = random.choices(population, weights)[0]
        parent2 = random.choices(population, weights)[0]

        child1, child2 = crossover_function(parent1, parent2)

        # Perform mutation
        if random.random() < mutation_rate: # 20% chance of mutation change as needed
            child1 = make_mutation(child1)
        if random.random() < mutation_rate:
            child2 = make_mutation(child2)

        new_population.append(child1)
        new_population.append(child2)

    return new_population


def choose_new_population(population, new_population, fitness_function=get_makespan):
    # Combine the old and new populations
    combined_population = population + new_population

    # Get the fitness of each chromosome in the combined population
    fitness = [1 / fitness_function(machine_phases(chromosome)) for chromosome in combined_population]

    # Sort the combined population based on fitness
    combined_population = [chromosome for _, chromosome in
                           sorted(zip(fitness, combined_population), key=lambda x: x[0], reverse=True)]

    # Choose the top chromosomes to form the new population
    return combined_population[:len(population)]


def genetic_algorithm(jobs, population_size=8, generations=10,
                      mutation_rate=0.01, fitness_function=get_makespan, satisfication_vlue=0,
                      crossover_function=make_crossover): #print the progress percentage

    best_make_spans = set()
    worst_make_spans = set()
    population = create_chromosome(jobs, population_size)
    best_chromosome = population[0]
    gen = 0 #the generation in wich the best chromosome was found

    for generation in range(generations):
        weights = get_weights(population)
        new_population = generate_new_population(population, weights, population_size , mutation_rate, crossover_function)
        population = choose_new_population(population, new_population)

        if fitness_function(machine_phases(population[0])) < fitness_function(machine_phases(best_chromosome)):
            best_chromosome = population[0]
            gen = generation



        if fitness_function(machine_phases(population[0])) <= satisfication_vlue:
            break

#       #get the best makespan
        best_make_spans.add(fitness_function(machine_phases(population[0])))
        worst_make_spans.add(fitness_function(machine_phases(population[-1])))
        # print(f"Generation {generation + 1}/{generations} completed")# for the progress percentage

    best_chromosome = population[0]
    machines_process = machine_phases(best_chromosome)
    # jobs = extract_jobs(machines_process)
    # draw_gantt_chart(machines_process, jobs)
    makespan = fitness_function(machines_process)

    # print("Best Chromosome")
    # for phase in best_chromosome:
    #     print(phase.__repr__())
    # print("Best Makespan")
    # print(makespan)
    # print("Best Makespans")
    # print(best_make_spans)
    # print("Worst Makespans")
    # print(worst_make_spans)
    return best_chromosome, makespan, gen

if __name__ == '__main__':
    Jobs = dictionary_store("../Data/job_shop_schedule.csv")
    population = create_chromosome(Jobs)

    for i in population:
        print(i)