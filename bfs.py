from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return None

def build_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the node names:")
    nodes = [input(f"Node {i+1}: ") for i in range(num_nodes)]

    for node in nodes:
        graph[node] = []

    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (format: node1 node2):")
    for _ in range(num_edges):
        u, v = input().split()
        if u in graph and v in graph:
            graph[u].append(v)
            graph[v].append(u)  # For undirected graph
        else:
            print(f"Invalid edge between {u} and {v}. One or both nodes not found.")

    return graph

def main():
    graph = build_graph()
    print("\nConstructed Graph:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    if start not in graph or goal not in graph:
        print("Start or goal node not found in the graph.")
        return

    path = bfs(graph, start, goal)
    if path:
        print(f"\nShortest path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"\nNo path found from {start} to {goal}.")

if __name__ == "__main__":
    main()