
from read_csv import dictionary_store
from genetic_algorithm import *

Jobs = dictionary_store("job_shop_schedule.csv")


population = create_chromosome(Jobs)


best_chromosome = None
best_makespan = float('inf')

for chromosome in population:
    machines_process = machine_phases(chromosome)
    jobs = extract_jobs(machines_process)
    draw_gantt_chart(machines_process, jobs)
    makespan = get_makespan(machines_process)
    if makespan < best_makespan:
        best_makespan = makespan
        best_chromosome = chromosome


print("Best Chromosome")
print(best_chromosome)
print("Best Makespan")
print(best_makespan)
machines_process = machine_phases(best_chromosome)
jobs = extract_jobs(machines_process)
draw_gantt_chart(machines_process, jobs)


make_crossover(population[0], population[1])

# the mutation is not correct
# print("before Mutation")
# for phase in population[0]:
#     print(phase.__repr__())
#
# print("makespan before Mutation")
# machines_process = machine_phases(population[0])
# print(get_makespan(machines_process))
#
# muted = make_mutation(population[0])
#
# print("make span After Mutation")
#
# machines_process = machine_phases(muted)
# print(get_makespan(machines_process))
#

