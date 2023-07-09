# Define function

def floyd_recursive(graph, n):
    if n == 0:
        return graph

    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return floyd_recursive(graph, n - 1)