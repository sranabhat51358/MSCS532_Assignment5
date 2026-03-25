# utils.py

import random


def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(size))


def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))
