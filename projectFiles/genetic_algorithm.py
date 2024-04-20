import copy


import random
import time

random.seed(time.time())

import matplotlib.pyplot as plt

from matplotlib.patches import Patch

from projectFiles.Job_Phases import *


def create_chromosome(Jobs, population_size = 7):

    population = set()
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
        population.add(tuple(chromosome))

    # Convert the set back to a list for consistency with the rest of your code
    population = list(population)

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
        machines_process[phase.machine] = {'process': [], 'finish_time': 0}
        jobs[phase.job] = {'available': True, 'order': 1, 'available_at': 0}


    #sort machines_process based on the number after M
    machines_process = dict(sorted(machines_process.items(), key=lambda x: int(x[0][1:])))

    # print(machines_process)

    jobs = dict(sorted(jobs.items()))

    chrom = list(chromosome)

    print(chrom)

    t = 0
    while True:
        # print("Time: ", t)
        #print machines that are available
        # for mach in machines_process:
        #     print(mach, machines_process[mach])

        for phase in chromosome:

            if jobs[phase.job]['available'] and jobs[phase.job]['order'] == phase.phase_order and machines_process[phase.machine]['finish_time'] <= t:
                # print("in the if statement")
                # print("Job: ", phase.job, "Machine: ", phase.machine, "Duration: ", phase.duration, "Start Time: ", t)
                jobs[phase.job]['available'] = False
                jobs[phase.job]['available_at'] = phase.duration + t - 1  # Adjust here

                machines_process[phase.machine]['finish_time'] = phase.duration + t

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


def draw_gantt_chart(machines_process, jobs):

    fig, ax = plt.subplots(figsize=(12, 8))

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
    ax.set_xticks(range(0, max([phase.start_time + phase.duration for machine in machines_process for phase in machines_process[machine]['process']]), 2))



    legend_patches = [Patch(color=color, label=job) for job, color in job_colors.items()]

    # Adjust the legend box
    ax.legend(handles=legend_patches, bbox_to_anchor=(1, 1), loc='upper left', prop={'size': 12}, fancybox=True, shadow=True, edgecolor='black', facecolor='white', framealpha=0.7)

    #start from 0
    ax.set_xlim(0, max([phase.start_time + phase.duration for machine in machines_process for phase in machines_process[machine]['process']]))

    plt.show()


def extract_jobs(machines_process):
    jobs = set()
    for machine_data in machines_process.values():
        for process_phase in machine_data['process']:
            jobs.add(process_phase.job)

    #sort the set based on the number after _
    jobs = sorted(jobs, key=lambda x: int(x.split("_")[1]))

    return jobs


def get_makespan(machines_process):  #this function is to get the makespan wich is the fitness function
    makespan = 0
    for machine_data in machines_process.values():
        makespan = max(makespan, machine_data['finish_time'])
    return makespan

def make_crossover(parent1, parent2):
    child1 = []
    child2 = []

    # Get the length of the chromosome
    chromosome_length = len(parent1)
    #get two random number less than the length of the chromosome TO MAKE THE CUTT
    cut1 = random.randint(1, chromosome_length - 3)
    cut2 = random.randint(cut1+1, chromosome_length - 2)



    print('length of chromosome: ', chromosome_length)

    print("Cut1: ", cut1)
    print("Cut2: ", cut2)

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


    print("Child1")
    for phase in child1:
        print(phase.__repr__())

    print("chromosome 1" )
    for phase in parent1:
        print(phase.__repr__())

    print("chromosome 2")
    for phase in parent2:
        print(phase.__repr__())

    print("makespan for child1")
    machines_process = machine_phases(child1)
    print(get_makespan(machines_process))

    draw_gantt_chart(machine_phases(child1), extract_jobs(machine_phases(child1)))


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
#     print("Mutation")
#     for phase in chromosome:
#         print(phase.__repr__())
#
#     return tuple(chromosome)
