import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(
        f"Data from CSV file '{file_path}' has been loaded. The first 5 rows are:")

    print(df.head())


#save csv id dictionary

def dictionary_store(file_path):
    Jobs = {}
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        phases = row["Phases"].split(" -> ")
        Jobs[row["Job"]] = []
        for phase in phases:
            machine, time = phase.split("[")
            Jobs[row["Job"]].append((machine, int(time[:-1])))
    return Jobs



# Example usage
Jobs = dictionary_store("job_shop_schedule.csv")
#print each job on a row
for job in Jobs:
    print(job, Jobs[job])

