## Algorithm Assignment 3: Greedy Approach

This repository contains Python implementations of classic Greedy Algorithms. These algorithms make the best local choice at each step to find a global solution.

## Included Files

### 1. Fractional Knapsack (`Knapsack.py`)
- **Goal:** Maximize the total value of items in a knapsack with a weight limit.
- **Greedy Strategy:** Sort items by their value-to-weight ratio and take the most valuable items first (including fractions).

### 2. Job Sequencing with Profit (`job_sequence.py`)
- **Goal:** Maximize total profit by scheduling jobs within their deadlines.
- **Greedy Strategy:** Sort jobs by profit in descending order and assign them to the latest possible available time slot before their deadline.

## How to Run
Run the files using Python in your terminal:
```bash
python Knapsack.py
python job_sequence.py
