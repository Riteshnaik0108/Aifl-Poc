def dls(graph, start, limit):
    visited = set()
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()
        if node not in visited and depth <= limit:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))

# Input and execution
graph = {}
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start_node = input("Enter start node: ")
depth_limit = int(input("Enter depth limit: "))
print(f"DLS traversal (limit {depth_limit}):")
dls(graph, start_node, depth_limit)
