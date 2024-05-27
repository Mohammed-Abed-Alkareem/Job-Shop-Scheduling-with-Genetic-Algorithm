<p align="center">
    <h1 align="center">Optimizing Job Shop Scheduling in a Manufacturing Plant using Genetic Algorithm</h1>
</p>

<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>


## Overview

This repository contains the project "Optimizing Job Shop Scheduling in a Manufacturing Plant using Genetic Algorithm". The primary objective of this project is to demonstrate the application of genetic algorithms to optimize job shop scheduling, enhancing manufacturing efficiency.

## Repository Structure
```
└── Job-Shop-Scheduling-with-Genetic-Algorithm/
    ├── ENCS3340_Project_1.pdf
    ├── README.md
    ├── Report
    │   ├── Report_Project_1211250_1210708.docx
    │   ├── Report_Project_1211250_1210708.pdf
    │   └── ScreenShots
    │       ├── Makespan_Gantt-Chart.png
    │       ├── Standard_Deviation_Gantt-Chart.png
    │       └── Working_Time_Gantt-Chart.png
    ├── projectFiles
    │   ├── Analysis.ipynb
    │   ├── Data
    │   │   ├── __init__.py
    │   │   ├── generate_data.py
    │   │   ├── job_shop_schedule.csv
    │   │   └── read_csv.py
    │   ├── GUI.py
    │   ├── Genetic_Algoritm
    │   │   ├── Crossover_Functions.py
    │   │   ├── Fitness_Functions.py
    │   │   ├── Job_Phases.py
    │   │   ├── Mutations.py
    │   │   ├── __init__.py
    │   │   └── genetic_algorithm.py
    │   ├── __init__.py
    │   ├── collect_data.ipynb
    │   └── main.py
    └── results
        ├── alternating_parental_gene_crossover.csv
        ├── alternating_parental_gene_crossover_scramble_mutation.csv
        ├── double_segment_crossover.csv
        ├── double_segment_crossover_scramble_mutation.csv
        ├── partially_mapped_crossover.csv
        ├── partially_mapped_crossover_scramble_mutation.csv
        ├── single_segment_crossover.csv
        └── single_segment_crossover_scramble_mutation.csv
```

##  Modules

<details closed><summary>projectFiles</summary>

| File                                                                                                                                                   | Summary                                                     |
| ---                                                                                                                                                    | ---                                                         |
| [Analysis.ipynb](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Analysis.ipynb)         | jupyter notebook for making the analysis `projectFiles/Analysis.ipynb`     |
| [GUI.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/GUI.py)                         | a simple GUI `projectFiles/GUI.py`             |
| [collect_data.ipynb](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/collect_data.ipynb) | jupyter notebook for collecting the data `projectFiles/collect_data.ipynb` |

</details>

<details closed><summary>projectFiles.Genetic_Algoritm</summary>

| File                                                                                                                                                                            | Summary                                                                          |
| ---                                                                                                                                                                             | ---                                                                              |
| [Fitness_Functions.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Genetic_Algoritm/Fitness_Functions.py)     | python file containing the fitness functions `projectFiles/Genetic_Algoritm/Fitness_Functions.py`   |
| [genetic_algorithm.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Genetic_Algoritm/genetic_algorithm.py)     | python file containing the genetic algorithm functions `projectFiles/Genetic_Algoritm/genetic_algorithm.py`   |
| [Mutations.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Genetic_Algoritm/Mutations.py)                     | python file containing the mutations functions  `projectFiles/Genetic_Algoritm/Mutations.py`           |
| [Job_Phases.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Genetic_Algoritm/Job_Phases.py)                   | python file containing the classes `projectFiles/Genetic_Algoritm/Job_Phases.py`          |
| [Crossover_Functions.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Genetic_Algoritm/Crossover_Functions.py) | python file containing the crossovers functions  `projectFiles/Genetic_Algoritm/Crossover_Functions.py` |

</details>

<details closed><summary>projectFiles.Data</summary>

| File                                                                                                                                                    | Summary                                                        |
| ---                                                                                                                                                     | ---                                                            |
| [generate_data.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Data/generate_data.py) | python file that generate random data `projectFiles/Data/generate_data.py` |
| [read_csv.py](https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm/blob/master/projectFiles/Data/read_csv.py)           | csv files containing the jobs and their phases `projectFiles/Data/read_csv.py`      |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.11.0`

###  Installation

1. Clone the Job-Shop-Scheduling-with-Genetic-Algorithm repository:

```sh
git clone https://github.com/Mohammed-Abed-Alkareem/Job-Shop-Scheduling-with-Genetic-Algorithm
```

2. Change to the project directory:

```sh
cd Job-Shop-Scheduling-with-Genetic-Algorithm
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running Job-Shop-Scheduling-with-Genetic-Algorithm

Use the following command to run Job-Shop-Scheduling-with-Genetic-Algorithm:

```sh
python GUI.py
```

## Contents

1. [Introduction](#introduction)
2. [Problem Formulation](#problem-formulation)
   - [Description of the Problem](#description-of-the-problem)
   - [Goals](#goals)
   - [Problem Formulation Components](#problem-formulation-components)
3. [Genetic Algorithm Implementation](#genetic-algorithm-implementation)
   - [Problem Representation](#problem-representation)
   - [Fitness Functions](#fitness-functions)
   - [Crossover Methods](#crossover-methods)
   - [Mutation Methods](#mutation-methods)
4. [Analysis](#analysis)
   - [Data Collection](#data-collection)
   - [Descriptive Analysis](#descriptive-analysis)
   - [Inferential Analysis](#inferential-analysis)
   - [Confidence Interval Analysis](#confidence-interval-analysis)
5. [Test Cases](#test-cases)
   - [Make Span](#make-span)
   - [Working Time](#working-time)
   - [Standard Deviation](#standard-deviation)
6. [Conclusion](#conclusion)
7. [References](#references)

## Introduction

Job shop scheduling is a critical challenge in manufacturing where multiple products require various operations on different machines. Efficient scheduling minimizes production time and maximizes operational efficiency. This project uses a genetic algorithm to address job shop scheduling, aiming to optimize the sequence and timing of operations.

## Problem Formulation

### Description of the Problem

In a manufacturing plant, job shop scheduling involves assigning a series of operations to various machines. Each job consists of a sequence of operations on specific machines for certain durations. The goal is to find an optimal schedule for these jobs.

### Goals

The genetic algorithm aims to:
- Minimize Total Completion Time
- Minimize Average Working Time
- Minimize Standard Deviation of Machine Completion Time

### Problem Formulation Components

- **Initial State**: A randomly generated schedule.
- **Actions**: Applying crossover and mutation operations.
- **Transition Model**: Successor functions include crossover and mutation.
- **Goal State**: A schedule that optimally satisfies the defined fitness functions.

## Genetic Algorithm Implementation

### Problem Representation

1. **Initial Population**: A set of chromosomes representing possible schedules.
2. **Chromosome Structure**: Each chromosome includes job ID, machine order, machine, and time required.
3. **Fitness Calculation**: Fitness functions evaluate each chromosome's schedule quality.
4. **Selection**: Techniques like roulette wheel selection based on fitness values.
5. **Crossover**: Methods to generate offspring from parent chromosomes.
6. **Mutation**: Introduce variability in the population.
7. **Survivor Selection**: The fittest individuals form the next generation.
8. **Iteration**: Repeat until termination conditions are met.

### Fitness Functions

- **Minimize Total Completion Time**
- **Minimize Average Working Time**
- **Minimize Standard Deviation of Machine Completion Time**

### Crossover Methods

1. Single Segment Crossover
2. Double Segment Crossover
3. Partially Mapped Crossover (PMX)
4. Alternating Parental Gene Crossover

### Mutation Methods

1. Swapping Mutation
2. Scramble Mutation

## Analysis

### Data Collection

- **Iterations**: 100 iterations per combination.
- **Generations**: Up to 500 generations per iteration.

### Descriptive Analysis

- **Single Segment Scramble**: Highest median normalized fitness and lowest variability.
- **Single Segment Swap**: High median fitness with consistent performance.
- **Partially Mapped Swap**: Good performance consistency with some variability.

### Inferential Analysis

- **Single Segment Swap**: Highest mean fitness with low variability.
- **Single Segment Scramble**: Very high mean fitness with consistent performance.
- **Partially Mapped Swap**: High mean fitness with moderate variability.

### Confidence Interval Analysis

- **Single Segment Swap**: Fewest generations for 95% probability of optimal fitness.
- **Single Segment Scramble**: Slightly more generations than Swap.
- **Partially Mapped Scramble**: Moderately efficient.




## Test Cases

### Make Span

- ![Make Span Gantt-Chart](/Report/ScreenShots/Makespan_Gantt-Chart.png)


### Working Time

- ![Working Time Gantt-Chart](/Report/ScreenShots/Working_Time_Gantt-Chart.png)

### Standard Deviation

- ![Standard Deviation Gantt-Chart](/Report/ScreenShots/Standard_Deviation_Gantt-Chart.png)

## Conclusion

The analysis concludes that the Single Segment Scramble method is the most effective for job shop scheduling, achieving high fitness values with low variability and requiring fewer generations.

