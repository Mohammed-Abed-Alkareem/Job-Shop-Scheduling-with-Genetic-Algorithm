import csv
import random


# Function to generate random job data
def generate_job_data(job_count, machine_count, max_phases, max_time):
    jobs = []
    for i in range(1, job_count + 1):
        phases_count = random.randint(1, max_phases)
        phases = []
        for j in range(1, phases_count + 1):
            machine = f"M{random.randint(1, machine_count)}"
            time = random.randint(1, max_time)
            phases.append(f"{machine}[{time}]")
        jobs.append({"Job": f"Job_{i}", "Phases": " -> ".join(phases)})
    return jobs


# Generate job data
job_count = 10  # Change this value to adjust the number of jobs
machine_count = 5  # Change this value to adjust the number of machines
max_phases = 3  # Maximum number of phases per job
max_time =20  # Maximum processing time for each phase
job_data = generate_job_data(job_count, machine_count, max_phases, max_time)

# Write data to CSV file
output_file = "job_shop_schedule.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Job", "Phases"])
    writer.writeheader()
    writer.writerows(job_data)

print(f"CSV file '{output_file}' with {job_count} jobs and {machine_count} machines has been created.")
