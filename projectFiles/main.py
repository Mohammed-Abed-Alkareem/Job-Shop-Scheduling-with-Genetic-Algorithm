import random
import time

from read_csv import dictionary_store
import copy

from Job_Phases import *

Jobs = dictionary_store("job_shop_schedule.csv")
random.seed(time.time())


def create_chromosome(Jobs, population_size = 10):

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
        jobs[phase.job] = {'available': True, 'order': 1, 'available_at':0}

    machines_process = dict(sorted(machines_process.items()))
    jobs = dict(sorted(jobs.items()))

    chrom = list(chromosome)

    print(chrom)

    t = 0
    while True:
        print("Time: ", t)
        for phase in chrom:
            if jobs[phase.job]['available'] and jobs[phase.job]['order'] == phase.phase_order and machines_process[phase.machine]['finish_time'] <= t:
                print("Job: ", phase.job, "Machine: ", phase.machine, "Duration: ", phase.duration, "Start Time: ", t)
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

        for phase in chrom:
            if jobs[phase.job]['available_at'] == t:
                print("yes")
                jobs[phase.job]['available'] = True

        if not chrom:
            break

        t += 1

    print("machines_process")
    for machine in machines_process:
        print(machine, machines_process[machine])

    print("jobs")
    for job in jobs:
        print(job, jobs[job])

    return machines_process





import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Patch

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



population = create_chromosome(Jobs)



for chromosome in population:
    machines_process = machine_phases(chromosome)
    jobs = extract_jobs(machines_process)
    draw_gantt_chart(machines_process, jobs)
