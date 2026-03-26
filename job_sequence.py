def job_sequencing(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(min(max_deadline, deadline) - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                total_profit += profit
                break
                
    return [j for j in schedule if j is not None], total_profit

if __name__ == "__main__":
    # (Job ID, Deadline, Profit)
    job_data = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
    sequence, profit = job_sequencing(job_data)
    print(f"Job Sequence: {sequence}")
    print(f"Total Profit: {profit}")
