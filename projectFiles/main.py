import random
import time

from read_csv import dictionary_store
import copy

from Job_Phases import *

Jobs = dictionary_store("job_shop_schedule.csv")
random.seed(time.time())


def create_chromosome(Jobs, population_size = 20):

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

    print("Population")

    for chromosome in population:
        # print(chromosome)
        # print(len(chromosome))
        print("_____________________________________________________")
        for phase in chromosome:
            print(phase.__repr__())

    print(x)
    return population


def machine_phases(chromosome):

    machines_process = {}  #the dictionary for machines phase order
    jobs = {}  # to store weather if a job is currently working

    for phase in chromosome:
        machines_process[phase.machine] = {'process': [], 'finish_time': 0}
        jobs[phase.job] = {'available': True, 'order': 1}

    machines_process = dict(sorted(machines_process.items()))
    jobs = dict(sorted(jobs.items()))

    chrom = list(chromosome)



    print(chrom)

    # t = 0
    # while True:
    #
    #     if not chrom:
    #         print("yes")
    #         break

        # for phase in chromosome:
        #     if jobs[phase.job][0] and machines_process[phase.machine][finish_time] <= t:
        #
        #         jobs[phase.job][0] = False
        #
        #         machines_process[phase.machine][0].append(
        #             ProcessPhases(job=phase.job,
        #                           phase_order=phase.phase_order,
        #                           machine=phase.machine,
        #                           duration=phase.duration,
        #                           start_time=t
        #                           )
        #         )
        #
        # if t == 5:
        #     break
        #
        # t += 1


    print(machines_process)
    print(jobs)





population = create_chromosome(Jobs)

machine_phases(population[0])