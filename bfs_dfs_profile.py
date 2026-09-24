import time
from collections import deque


# ---------------- BFS ----------------
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return visited


# ---------------- DFS ----------------
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited


# ---------------- Graph Creation ----------------

# Best Case: 10-vertex sparse tree
def best_case_graph():
    graph = {i: [] for i in range(10)}

    edges = [
        (0, 1), (0, 2),
        (1, 3), (1, 4),
        (2, 5), (2, 6),
        (3, 7),
        (4, 8),
        (5, 9)
    ]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph


# Average Case: K10 complete graph
def average_case_graph():
    graph = {i: [] for i in range(10)}

    for i in range(10):
        for j in range(i + 1, 10):
            graph[i].append(j)
            graph[j].append(i)

    return graph


# Worst Case: K20 complete graph
def worst_case_graph():
    graph = {i: [] for i in range(20)}

    for i in range(20):
        for j in range(i + 1, 20):
            graph[i].append(j)
            graph[j].append(i)

    return graph


# ---------------- Timing Function ----------------

def measure_time(function, graph, repetitions=10000):

    start_time = time.perf_counter()

    for _ in range(repetitions):
        function(graph, 0)

    end_time = time.perf_counter()

    return (end_time - start_time) * 1000


# ---------------- Run Test ----------------

def run_test(test_name, graph):

    bfs_times = []
    dfs_times = []

    for _ in range(3):

        bfs_time = measure_time(bfs, graph)
        dfs_time = measure_time(dfs, graph)

        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)

    bfs_average = sum(bfs_times) / 3
    dfs_average = sum(dfs_times) / 3

    print("\n====================================")
    print(test_name)
    print("====================================")

    print("\nBFS:")
    print("Run 1:", round(bfs_times[0], 3), "ms")
    print("Run 2:", round(bfs_times[1], 3), "ms")
    print("Run 3:", round(bfs_times[2], 3), "ms")
    print("Average:", round(bfs_average, 3), "ms")

    print("\nDFS:")
    print("Run 1:", round(dfs_times[0], 3), "ms")
    print("Run 2:", round(dfs_times[1], 3), "ms")
    print("Run 3:", round(dfs_times[2], 3), "ms")
    print("Average:", round(dfs_average, 3), "ms")


# ---------------- Main Program ----------------

best_graph = best_case_graph()
average_graph = average_case_graph()
worst_graph = worst_case_graph()

# Display traversal order for the best-case graph
print("BFS Best Case Traversal:")
print(bfs(best_graph, 0))

print("\nDFS Best Case Traversal:")
print(dfs(best_graph, 0))

# Run all three test cases
run_test("BEST CASE - 10 Vertex Sparse Tree", best_graph)
run_test("AVERAGE CASE - K10 Complete Graph", average_graph)
run_test("WORST CASE - K20 Complete Graph", worst_graph)
