############################################
# MSCS 532 Final Project (Part 1)
# Author: Gregory Renteria
# Implementation of naive and optimized
# versions of the pairwise absolute
# difference sum problem + benchmarking
############################################

import time
import numpy as np
import matplotlib.pyplot as plt

def pairwise_sum_naive(points):
    total = 0.0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            total += abs(points[i] - points[j])
    return total

def pairwise_sum_vectorized(points):
    arr = np.array(points)
    diff_matrix = np.abs(arr[:, None] - arr[None, :])
    return np.sum(np.triu(diff_matrix, k=1))  # Sum only upper triangle (excluding diagonal)

# Input sizes to test
sizes = [1000, 2000, 5000, 10000]
naive_times = []
optimized_times = []
speedups = []

# Benchmarking loop
for size in sizes:
    data = np.random.rand(size)

    # Naive
    start = time.time()
    result_naive = pairwise_sum_naive(data)
    naive_time = time.time() - start
    naive_times.append(naive_time)

    # Optimized
    start = time.time()
    result_opt = pairwise_sum_vectorized(data)
    optimized_time = time.time() - start
    optimized_times.append(optimized_time)

    # Speedup
    speedup = naive_time / optimized_time if optimized_time > 0 else float('inf')
    speedups.append(speedup)

    # Ensure correctness
    assert np.isclose(result_naive, result_opt), f"Mismatch at size {size}"

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, naive_times, label='Naive (O(n²))', marker='o')
plt.plot(sizes, optimized_times, label='Optimized (Vectorized)', marker='o')
plt.title('Execution Time Comparison')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()

ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(sizes, speedups, color='green', linestyle='--', marker='x', label='Speedup (Naive / Optimized)')
ax2.set_ylabel('Speedup Factor')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()