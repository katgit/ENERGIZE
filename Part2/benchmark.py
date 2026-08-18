"""Simple CPU benchmark for the Part 2 qsub example."""

import time

import numpy as np


def main():
    matrix_size = 1000
    repetitions = 3
    random_generator = np.random.default_rng(42)
    left_matrix = random_generator.random((matrix_size, matrix_size))
    right_matrix = random_generator.random((matrix_size, matrix_size))

    start_time = time.perf_counter()
    result_matrix = None
    for _ in range(repetitions):
        result_matrix = left_matrix @ right_matrix
    elapsed_seconds = time.perf_counter() - start_time

    print(f"Matrix size: {matrix_size} x {matrix_size}")
    print(f"Repetitions: {repetitions}")
    print(f"Elapsed time: {elapsed_seconds:.3f} seconds")
    print(f"Result checksum: {result_matrix.sum():.6f}")


if __name__ == "__main__":
    main()
