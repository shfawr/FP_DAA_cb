BENCHMARK_SEED = 42

# Grid sizes (N x N). N^2 is the number of vertices.
# 32^2 = 1,024  ...  256^2 = 65,536 (>= 2 orders of magnitude)
BENCHMARK_SIZES = [32, 64, 96, 128, 256]

# Number of mazes (instances) per size
BENCHMARK_TRIALS = 5
