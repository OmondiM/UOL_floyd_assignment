import timeit
import random

# The function to be tested
def floyd_recursive(graph, n):
    if n == 0:
        return graph

    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return floyd_recursive(graph, n - 1)


# Function to generate a random graph of a given size
def generate_graph(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]


# Performance testing function
def test_performance():
    sizes = [10, 50]  # Sizes of graphs to test
    num_trials = 10  # Number of trials for each size

    for size in sizes:
        total_time = 0

        for _ in range(num_trials):
            graph = generate_graph(size)

            start_time = timeit.default_timer()
            floyd_recursive(graph, size)
            end_time = timeit.default_timer()

            total_time += end_time - start_time

        average_time = total_time / num_trials

        print(f"Average time for size {size}: {average_time}")


# Run the performance test
test_performance()
