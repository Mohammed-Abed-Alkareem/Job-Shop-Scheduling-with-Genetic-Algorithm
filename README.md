
# Optimizing Job Shop Scheduling in a Manufacturing Plant using Genetic Algorithm

## Overview

This repository contains the project "Optimizing Job Shop Scheduling in a Manufacturing Plant using Genetic Algorithm". The primary objective of this project is to demonstrate the application of genetic algorithms to optimize job shop scheduling, enhancing manufacturing efficiency.

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

- ![Make Span Gantt-Chart](Job-Shop-Scheduling-with-Genetic-Algorithm/Report/ScreenShots/Makespan-Gantt-Chart.png)


### Working Time

- **Figure 7-2**: Gantt chart for working time.

### Standard Deviation

- **Figure 7-3**: Gantt chart for standard deviation.

## Conclusion

The analysis concludes that the Single Segment Scramble method is the most effective for job shop scheduling, achieving high fitness values with low variability and requiring fewer generations.

