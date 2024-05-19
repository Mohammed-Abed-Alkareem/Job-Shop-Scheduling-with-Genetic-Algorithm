import statistics


# Completion time
def get_makespan(machines_process):  #this function is to get the makespan wich is the fitness function
    '''This function is to get the makespan of the machines'''
    makespan = 0
    for machine_data in machines_process.values():
        makespan = max(makespan, machine_data['finish_time'])

    return makespan

# Working time
def get_working_time(machines_process):  #this function is to get the makespan which is the fitness function
    '''This function is to get the working time of the machines'''
    #summation of all machines makespan - start time
    working_time = 0
    for machine_data in machines_process.values():
        working_time += machine_data['finish_time'] - machine_data['start_time']

    return working_time


# Standard Deviation of machines Completion time
def get_machines_standard_deviation(machines_process):
    completion_times = []
    for machine_data in machines_process.values():
        completion_times.append(machine_data['finish_time'])

    if len(completion_times) > 1:
        standard_deviation = statistics.stdev(completion_times)
    else:
        standard_deviation = 0

    return standard_deviation


def combination_fitnesses(*args):  # just a sample
    '''This function is to get the combination of the fitness functions'''
    #set weights for each fitness function
    weights = [1 / len(args) for _ in args]
    #get the fitness value for each function
    fitness_values = [weight * fitness_function for weight, fitness_function in zip(weights, args)]
    #return the sum of the fitness values
    return sum(fitness_values)
