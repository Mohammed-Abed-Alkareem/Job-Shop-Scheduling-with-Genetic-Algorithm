#this is a test code from chatgpt

import numpy as np
import random


class Job:
    def __init__(self, name, operations):
        self.name = name
        self.operations = operations


class Machine:
    def __init__(self, name):
        self.name = name
        self.current_job = None
        self.current_operation = 0
        self.current_time = 0


class Schedule:
    def __init__(self, machines):
        self.machines = machines


def generate_random_schedule(jobs, machines):
    schedule = Schedule(machines)
    for job in jobs:
        machine_index = random.randint(0, len(machines) - 1)
        schedule.machines[machine_index].current_job = job
    return schedule


def evaluate_schedule(schedule):
    max_time = 0
    for machine in schedule.machines:
        if machine.current_job:
            max_time = max(max_time,
                           machine.current_time + machine.current_job.operations[machine.current_operation][1])
    return max_time


def genetic_algorithm(jobs, num_machines, population_size, generations):
    machines = [Machine(f"M{i + 1}") for i in range(num_machines)]
    population = [generate_random_schedule(jobs, machines) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: evaluate_schedule(x))
        elite = population[:population_size // 2]
        new_population = elite

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(elite, 2)
            crossover_point = random.randint(1, len(parent1.machines) - 1)
            child_schedule = Schedule([Machine(machine.name) for machine in parent1.machines])

            for i in range(len(child_schedule.machines)):
                if i < crossover_point:
                    child_schedule.machines[i].current_job = parent1.machines[i].current_job
                    child_schedule.machines[i].current_operation = parent1.machines[i].current_operation
                    child_schedule.machines[i].current_time = parent1.machines[i].current_time
                else:
                    child_schedule.machines[i].current_job = parent2.machines[i].current_job
                    child_schedule.machines[i].current_operation = parent2.machines[i].current_operation
                    child_schedule.machines[i].current_time = parent2.machines[i].current_time

            # Mutation
            mutation_probability = 0.1
            for machine in child_schedule.machines:
                if random.random() < mutation_probability:
                    machine.current_operation = random.randint(0, len(machine.current_job.operations) - 1)

            new_population.append(child_schedule)

        population = new_population

    best_schedule = min(population, key=lambda x: evaluate_schedule(x))
    return best_schedule


# Example usage
job1 = Job("Job_1", [("M1", 10), ("M2", 5), ("M4", 12)])
job2 = Job("Job_2", [("M2", 7), ("M3", 15), ("M1", 8)])
jobs = [job1, job2]

num_machines = 3
population_size = 10
generations = 100

best_schedule = genetic_algorithm(jobs, num_machines, population_size, generations)
for machine in best_schedule.machines:
    print(f"Machine {machine.name}:")
    if machine.current_job:
        print(f"   Current Job: {machine.current_job.name}")
        print(f"   Current Operation: {machine.current_operation}")
        print(f"   Current Time: {machine.current_time}")
    else:
        print("   Idle")
