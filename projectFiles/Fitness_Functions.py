

def get_makespan(machines_process):  #this function is to get the makespan wich is the fitness function
    makespan = 0
    for machine_data in machines_process.values():
        makespan = max(makespan, machine_data['finish_time'])

    return makespan

def get_working_time(machines_process):  #this function is to get the makespan wich is the fitness function
    #summation of all machines makespan - start time
    working_time = 0
    for machine_data in machines_process.values():
        working_time += machine_data['finish_time'] - machine_data['start_time']

    return working_time