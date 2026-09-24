from collections import deque

# ============================================================
# BFS vs DFS - All Three Cases from the Report
#
# 1. BEST CASE   : 10-vertex sparse tree, 9 edges
# 2. AVERAGE CASE: Complete graph K10, 10 vertices, 45 edges
# 3. WORST CASE  : Complete graph K20, 20 vertices, 190 edges
#
# Start vertex = 0
#
# The tree printed for each case is the TRAVERSAL TREE
# (the first time each vertex is reached). For K10 and K20,
# the original graph is complete, so its full graph cannot be
# displayed as a simple tree without showing all edges.
# ============================================================


# ------------------------------------------------------------
# BFS
# ------------------------------------------------------------
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# ------------------------------------------------------------
# DFS
# ------------------------------------------------------------
def dfs(graph, start):
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


# ------------------------------------------------------------
# BFS traversal tree
# ------------------------------------------------------------
def bfs_tree(graph, start):
    visited = {start}
    queue = deque([start])
    children = {v: [] for v in graph}

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                children[vertex].append(neighbor)
                queue.append(neighbor)

    return children


# ------------------------------------------------------------
# DFS traversal tree
# ------------------------------------------------------------
def dfs_tree(graph, start):
    visited = set()
    children = {v: [] for v in graph}

    def visit(vertex):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                children[vertex].append(neighbor)
                visit(neighbor)

    visit(start)
    return children


# ------------------------------------------------------------
# Print a traversal tree using branches
# ------------------------------------------------------------
def print_traversal_tree(children, root):
    print(root)

    def show(vertex, prefix=""):
        child_list = children[vertex]

        for i, child in enumerate(child_list):
            is_last = i == len(child_list) - 1
            connector = "└── " if is_last else "├── "
            print(prefix + connector + str(child))

            next_prefix = prefix + ("    " if is_last else "│   ")
            show(child, next_prefix)

    show(root)


# ------------------------------------------------------------
# Graph creation helpers
# ------------------------------------------------------------
def make_empty_graph(n):
    return {i: [] for i in range(n)}


def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


# ------------------------------------------------------------
# BEST CASE
# 10 vertices, 9 edges
# Uses the same tree structure requested by the user.
# ------------------------------------------------------------
def make_best_case():
    graph = make_empty_graph(10)

    edges = [
        (0, 1), (0, 2),
        (1, 3), (1, 4),
        (2, 5), (2, 6),
        (3, 7),
        (4, 8),
        (5, 9)
    ]

    for u, v in edges:
        add_edge(graph, u, v)

    return graph


# ------------------------------------------------------------
# AVERAGE CASE
# Complete graph K10
# 10 vertices, 45 edges
# ------------------------------------------------------------
def make_complete_graph(n):
    graph = make_empty_graph(n)

    for u in range(n):
        for v in range(u + 1, n):
            add_edge(graph, u, v)

    # Keep traversal deterministic.
    for vertex in graph:
        graph[vertex].sort()

    return graph


# ------------------------------------------------------------
# Run and display one test case
# ------------------------------------------------------------
def run_case(name, graph):
    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    print("\nBFS Traversal:")
    bfs_order = bfs(graph, 0)
    print(" -> ".join(map(str, bfs_order)))

    print("\nBFS Traversal Tree:")
    print_traversal_tree(bfs_tree(graph, 0), 0)

    print("\nDFS Traversal:")
    dfs_order = dfs(graph, 0)
    print(" -> ".join(map(str, dfs_order)))

    print("\nDFS Traversal Tree:")
    print_traversal_tree(dfs_tree(graph, 0), 0)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    best_case = make_best_case()
    average_case = make_complete_graph(10)
    worst_case = make_complete_graph(20)

    print("=" * 70)
    print("BFS vs DFS GRAPH TRAVERSAL - THREE CASES")
    print("=" * 70)

    run_case(
        "BEST CASE - 10 VERTICES, 9 EDGES (SPARSE TREE)",
        best_case
    )

    run_case(
        "AVERAGE CASE - COMPLETE GRAPH K10 (10 VERTICES, 45 EDGES)",
        average_case
    )

    run_case(
        "WORST CASE - COMPLETE GRAPH K20 (20 VERTICES, 190 EDGES)",
        worst_case
    )

    print("\n" + "=" * 70)
    print("COMPLEXITY")
    print("=" * 70)
    print("BFS: Θ(V + E)")
    print("DFS: Θ(V + E)")
    print("Auxiliary space: Θ(V)")


if __name__ == "__main__":
    main()
