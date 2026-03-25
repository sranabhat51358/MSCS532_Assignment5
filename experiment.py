# experiment.py

import time
import copy

from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort
from utils import (
    generate_random_array,
    generate_sorted_array,
    generate_reverse_sorted_array,
)


def measure_time(sort_func, arr):
    """
    Measure execution time
    """
    start = time.perf_counter()
    sort_func(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    return end - start


def safe_measure(sort_func, arr):
    """
    Prevent crash due to RecursionError
    """
    try:
        return measure_time(sort_func, arr)
    except RecursionError:
        return float("inf")  # mark failure


def format_time(t):
    """
    Pretty print results
    """
    if t == float("inf"):
        return "RecursionError"
    return f"{t:.6f} seconds"


def run_experiment():
    sizes = [100, 500, 1000, 5000, 10000]

    generators = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array,
    }

    print("\n=== Quicksort Performance Comparison ===\n")

    for size in sizes:
        print(f"\nArray Size: {size}")
        print("-" * 40)

        for name, generator in generators.items():
            arr = generator(size)

            arr1 = copy.deepcopy(arr)
            arr2 = copy.deepcopy(arr)

            # Deterministic (safe)
            time_det = safe_measure(quicksort, arr1)

            # Randomized
            time_rand = safe_measure(randomized_quicksort, arr2)

            print(f"{name} Input:")
            print(f"  Deterministic: {format_time(time_det)}")
            print(f"  Randomized   : {format_time(time_rand)}")
            print()


if __name__ == "__main__":
    run_experiment()
