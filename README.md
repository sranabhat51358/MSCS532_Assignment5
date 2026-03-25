# MSCS532_Assignment5
This project focuses on the Quicksort algorithm, i implement both deterministic and randomized versions, and analyze their performance under different conditions.

## Project Structure
```
.
├── deterministic_quicksort.py     # Deterministic Quicksort implementation
├── randomized_quicksort.py        # Randomized Quicksort implementation
├── experiment.py                  # Performance comparison
├── utils.py                       # Random dataset generator
├── Assignment 5.pdf               # Project Report
├── README.md                      # Project documentation
```


## How to Run
### Clone Repository
```
git clone https://github.com/sranabhat51358/MSCS532_Assignment5.git
cd MSCS532_Assignment5
```
### Run Deterministic Quicksort
```
python deterministic_quicksort.py
```
#### Output
```
Sorted array: [1, 5, 7, 8, 9, 10]
```
### Run Randomized Quicksort
```
python experiment_heapsort.py
```

#### Output
```
Sorted array: [1, 5, 7, 8, 9, 10]
```

### Run Experiment for performance comparison
```
python experiment.py
```

#### Output
```
=== Quicksort Performance Comparison ===


Array Size: 100
----------------------------------------
Random Input:
  Deterministic: 0.000043 seconds
  Randomized   : 0.000067 seconds

Sorted Input:
  Deterministic: 0.000233 seconds
  Randomized   : 0.000060 seconds

Reverse Sorted Input:
  Deterministic: 0.000164 seconds
  Randomized   : 0.000060 seconds


Array Size: 500
----------------------------------------
Random Input:
  Deterministic: 0.000321 seconds
  Randomized   : 0.000413 seconds

Sorted Input:
  Deterministic: 0.005736 seconds
  Randomized   : 0.000382 seconds

Reverse Sorted Input:
  Deterministic: 0.004250 seconds
  Randomized   : 0.000372 seconds


Array Size: 1000
----------------------------------------
Random Input:
  Deterministic: 0.000604 seconds
  Randomized   : 0.000851 seconds

Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.000664 seconds

Reverse Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.000647 seconds


Array Size: 5000
----------------------------------------
Random Input:
  Deterministic: 0.003496 seconds
  Randomized   : 0.004149 seconds

Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.004044 seconds

Reverse Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.003926 seconds


Array Size: 10000
----------------------------------------
Random Input:
  Deterministic: 0.007453 seconds
  Randomized   : 0.009263 seconds

Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.008202 seconds

Reverse Sorted Input:
  Deterministic: RecursionError
  Randomized   : 0.008529 seconds
```

### Summary

The efficiency of Quicksort is very dependent on the effectiveness with which the pivot/array is segmented each time a recursion step is undertaken. This behavior is well explained through the theoretical complexity and experimental processes.

In both best and average cases, the pivot breaks down the array into fairly balanced subarrays. This makes the recursion tree with logarithmic height and also the time complexity of O(n log n). This tendency is manifested in the experimental results of random inputs. For example, at the input size of 10, 000, the deterministic version required 0.007453 seconds, whereas the randomized version required 0.009263 seconds, both exhibiting efficient scaling.

The worst-case, however, comes when we take the pivot to generate highly unbalanced partitions each time. It is especially clear when the input array is either sorted or reverse sorted. These instances would make the size of the problem reduced by a single element per recursive call leading to a time complexity of O(n²).

This theoretical behavior is highly supported by the results of the experiment. For example:
- At size 500 (sorted input), deterministic Quicksort took 0.005736 seconds, which is much slower than when reading random input (0.000321 seconds).
- At size 1000 and above, the deterministic implementation failed entirely with a RecursionError, indicating excessive recursion depth.

This is due to the fact that the recursion level is linear with the input size and thus it surpasses the default recursion limit of Python. It is not either an abstract problem, but a practical constraint that will directly impact the usability of the algorithms.

Regarding the space complexity, Quicksort is recursive in nature and thus, to the degree of recursion, it uses a stack space that is proportional to the depth of the recursion. In the balanced cases, it is still O(log n), but in the worst-case, it can become O(n) and, that is why, the run-time failures have been observed.