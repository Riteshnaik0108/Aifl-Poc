import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        self.graph.setdefault(u, []).append((v, cost))

    def best_first_search(self, start, goal):
        visited = set()
        pq = [(0, start)]

        while pq:
            cost, node = heapq.heappop(pq)
            print(node, end=" ")
            if node == goal:
                print("\nGoal reached!")
                return
            visited.add(node)
            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))
        print("\nGoal not reachable.")

# Input and execution
g = Graph()
edges = int(input("Enter number of edges: "))
for _ in range(edges):
    u, v, w = input("Enter edge (u v weight): ").split()
    g.add_edge(u, v, int(w))

start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("Best First Search path:")
g.best_first_search(start, goal)
