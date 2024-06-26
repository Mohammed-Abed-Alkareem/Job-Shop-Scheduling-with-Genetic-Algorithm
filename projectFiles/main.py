
from projectFiles.Data.read_csv import dictionary_store
from projectFiles.Genetic_Algoritm.genetic_algorithm import create_chromosome
from projectFiles.Genetic_Algoritm.Crossover_Functions import *

Jobs = dictionary_store("Data/job_shop_schedule.csv")

#from projectFiles.Genetic_Algoritm.Crossover_Functions import cross_over

# population = create_chromosome(Jobs)


# best_chromosome = None
# best_makespan = float('inf')
#
# for chromosome in population:
#     machines_process = machine_phases(chromosome)
#     jobs = extract_jobs(machines_process)
#     draw_gantt_chart(machines_process, jobs)
#     makespan = get_makespan(machines_process)
#     if makespan < best_makespan:
#         best_makespan = makespan
#         best_chromosome = chromosome
#
#
# print("Best Chromosome")
# print(best_chromosome)
# print("Best Makespan")
# print(best_makespan)
# machines_process = machine_phases(best_chromosome)
# jobs = extract_jobs(machines_process)
# draw_gantt_chart(machines_process, jobs)



# make_crossover(population[0], population[1])


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

# get_weightes(population)
#calculate time take on the function
# import time
# start = time.time()
#
# # genetic_algorithm(jobs=Jobs, population_size=20, generations=100, mutation_rate=0.05, fitness_function=get_working_time, satisfication_vlue=500)
#
# genetic_algorithm(jobs=Jobs, population_size=20, generations=1000, mutation_rate=0.05, fitness_function=get_makespan, satisfication_vlue=120)
#
# end = time.time()
# print("Time taken to run the function")
# print(end - start)

pop = create_chromosome(Jobs)
for i in range(100000):
    c1, c2 =partially_mapped_crossover(pop[0], pop[1])


    if not check_order(c1):
        print("Error in order")





#run crossover for all the  each one with the others
# test = set()
# for i in range(0, len(pop)):
#     for j in range(i+1, len(pop)):
#         cross_over(pop[i], pop[j])





# a = correct_job_order(pop[0])
# b = pop[0]

#check if each element in a is in b
# print(a==b)


