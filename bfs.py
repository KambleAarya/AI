from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start], 0

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbours = graph.get(node, [])
            for neighbour, cost in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                if neighbour == goal:
                    total_cost = calculate_cost(graph, new_path)
                    return new_path, total_cost
                queue.append(new_path)
            visited.add(node)
    return None, None

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        neighbours = graph[path[i]]
        for neighbour, edge_cost in neighbours:
            if neighbour == path[i + 1]:
                cost += edge_cost
                break
    return cost

def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ").strip()
        graph[node] = []

    e = int(input("Enter number of edges: "))
    print("Enter edges as: from to cost")
    for _ in range(e):
        u, v, cost = input().split()
        cost = int(cost)
        graph[u].append((v, cost))
        # Uncomment below for undirected graph
        # graph[v].append((u, cost))

    return graph

if __name__ == "__main__":
    graph = input_graph()
    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    path, cost = bfs(graph, start, goal)
    if path:
        print(f"\n✅ Path from {start} to {goal}: {' -> '.join(path)}")
        print(f"🧮 Total path cost: {cost}")
    else:
        print("❌ No path found.")
