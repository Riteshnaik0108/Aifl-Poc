import heapq

def astar(graph, heuristics, start, goal):
    open_list = [(heuristics[start], start)]
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]

        for neighbor in graph[current]:
            new_cost = g_costs[current] + graph[current][neighbor]
            if new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(open_list, (new_cost + heuristics[neighbor], neighbor))

    return None

# Input and execution
graph = {}
nodes = set()
edges = int(input("Enter number of edges: "))
for _ in range(edges):
    u, v, w = input("Enter edge (u v weight): ").split()
    w = float(w)
    graph.setdefault(u, {})[v] = w
    graph.setdefault(v, {})  # Ensure bidirectional graph or update as needed
    nodes.update([u, v])

heuristic = {}
for node in nodes:
    heuristic[node] = float(input(f"Heuristic value for {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = astar(graph, heuristic, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
