"""PyTorch GPU benchmark for the Part 2 qsub example."""

import time

import torch


def main():
    if not torch.cuda.is_available():
        raise SystemExit("No CUDA-enabled GPU is available. Request a GPU node.")

    device = torch.device("cuda")
    matrix_size = 4000
    repetitions = 3
    random_generator = torch.Generator(device=device).manual_seed(42)
    left_matrix = torch.rand((matrix_size, matrix_size), device=device, generator=random_generator)
    right_matrix = torch.rand((matrix_size, matrix_size), device=device, generator=random_generator)

    torch.cuda.synchronize()
    start_time = time.perf_counter()
    result_matrix = None
    for _ in range(repetitions):
        result_matrix = left_matrix @ right_matrix
    torch.cuda.synchronize()
    elapsed_seconds = time.perf_counter() - start_time

    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Matrix size: {matrix_size} x {matrix_size}")
    print(f"Repetitions: {repetitions}")
    print(f"Elapsed time: {elapsed_seconds:.3f} seconds")
    print(f"Result checksum: {result_matrix.sum().item():.6f}")


if __name__ == "__main__":
    main()
