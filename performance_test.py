# Measure the runtime, speedup, CPU utilization, and memory usage of a given algorithm

import time
import psutil
import os

def performance_test(func, *args, **kwargs):
    # Get the CPU usage before executing the function
    process = psutil.Process(os.getpid())
    cpu_start = process.cpu_percent(interval = 0.1)

    # Get the memory usage before executing the function
    mem_start = process.memory_info().rss

    # Measure the runtime of the function
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    runtime = end_time - start_time

    # Get the CPU usage after executing the function
    cpu_end = process.cpu_percent(interval = 0.1)

    # Get the memory usage after executing the function
    mem_end = process.memory_info().rss

    # Print the performance metrics
    print(f"Runtime: {runtime:.6f} seconds")
    print(f"CPU utilization: {cpu_end - cpu_start:.2f}%")
    print(f"Memory usage: {(mem_end - mem_start) / 1024 / 1024:.2f} MB")
    print("\n")

    return result
