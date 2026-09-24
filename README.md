# IAI-SLE2
SLE-2: BFS vs DFS Profiling

Overview

This SLE-2 component profiles and compares two graph traversal algorithms:

Breadth-First Search (BFS)

Depth-First Search (DFS)

Both algorithms are tested on the same deterministic undirected connected graphs using an adjacency-list representation. The comparison focuses on execution time, traversal structure, graph density, and profiling information.

Algorithms

Breadth-First Search (BFS)

BFS uses a FIFO queue and explores vertices level by level.

Depth-First Search (DFS)

DFS uses recursion / an implicit LIFO stack and explores deeply before backtracking.

Problem Statement

The same undirected connected graphs are traversed from starting vertex 0. BFS and DFS are compared using:

Execution time

Traversal structure and order

Graph size and density

Profiling information

Auxiliary space requirements

Test Cases

The experiment uses the following graph cases:

Test Case

Graph

Vertices

Edges

Purpose

Best

Sparse tree

10

9

Small sparse graph

Average

K10

10

45

Denser graph

Worst

K20

20

190

Dense graph with largest workload

Profiling Method

The report uses:

Python time.perf_counter for timing

Manual traversal checks

A py-spy-style flame-graph view

3 timing runs for every test case

10,000 complete traversals within each measured run

The three measured batch times are averaged for the reported result.

Timing Results

Test Case

Algorithm

Run 1 (ms)

Run 2 (ms)

Run 3 (ms)

Average (ms)

Best

BFS

12.311

11.781

11.572

11.888

Best

DFS

16.287

15.529

15.665

15.827

Average

BFS

27.032

24.183

23.757

24.991

Average

DFS

24.246

24.490

31.642

26.793

Worst

BFS

74.630

74.309

70.610

73.183

Worst

DFS

68.172

67.106

66.468

67.249

Timing values are machine-dependent. The main algorithmic conclusion is based on the complexity analysis rather than the absolute timing values.

Complexity

For the adjacency-list implementation:

Algorithm

Time Complexity

Auxiliary Space

BFS

Θ(V + E)

Θ(V)

DFS

Θ(V + E)

Θ(V) worst case

Both algorithms mark each reachable vertex once and scan each adjacency-list entry once.

Practical Difference

Feature

BFS

DFS

Main data structure

Queue

Recursion / Stack

Exploration style

Level by level

Deep path first

Shortest path in an unweighted graph

Naturally finds minimum-edge path

Does not guarantee minimum-edge path

Typical applications

Level-order traversal, unweighted shortest path

Connectivity, cycle detection, backtracking

py-spy — Short Explanation

py-spy is a Python profiling tool that helps identify where a Python program spends its execution time. It works by sampling the running Python process periodically rather than requiring changes to the program's source code.

How py-spy Works

It attaches to a running Python program.

At regular intervals, it samples the program's current execution stack.

It records which functions are active most frequently.

The collected samples can be represented as a flame graph.

What the Flame Graph Means

In a flame graph, wider sections represent functions that appear in more profiling samples and therefore account for more of the observed execution activity. The graph helps identify which parts of the program are consuming the most execution time.

For this SLE-2 experiment, the flame-graph view is used to visualize the main traversal routine and the queue/recursive work involved in BFS and DFS.

Note: The submitted report describes the visualization as a py-spy-style profiling diagram, not as a native py-spy capture. This distinction is kept to avoid claiming that an actual py-spy recording was performed when the report does not establish that.

Profiling Visualization

The report contains:

Graph and node diagrams for the BFS vs DFS comparison

Average execution-time visualization on a log scale

Py-spy-style flame graphs for BFS and DFS

The flame-graph visualization is explicitly described in the report as a py-spy-style profiling diagram, rather than a falsely labelled native py-spy capture.

Key Observations

BFS and DFS have the same asymptotic traversal time for the adjacency-list implementation: Θ(V + E).

BFS explores the graph level by level using a queue.

DFS explores deeply before backtracking using recursion or a stack.

The dense K20 graph produces the largest adjacency-list workload in this experiment.

Execution-time measurements are machine-dependent, so they should be interpreted alongside the algorithmic complexity.

BFS naturally finds a minimum-edge path in an unweighted graph, while DFS does not guarantee this.

Conclusion

This SLE-2 component compares BFS and DFS on sparse and dense adjacency-list graphs. Both algorithms visit reachable vertices once and scan adjacency entries once, resulting in Θ(V + E) time complexity. BFS uses a queue and explores level by level, while DFS uses recursion or a stack and explores deeply before backtracking.

AI Contribution

AI tools were used to assist with:

Structuring the BFS-versus-DFS profiling report

Preparing graph/node diagrams

Organizing comparison tables

Explaining the complexity analysis

Formatting the document according to the supplied SLE-2 report template

Repository

GitHub: https://github.com/ParshwaBhavare?tab=repositories
