import heapq

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
            g_new = g + cost
            f_new = g_new + heuristics.get(neighbor, float('inf'))
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')

def build_graph():
    graph = {}
    heuristics = {}
    nodes = set()

    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge in the format: node1 node2 cost")
    for _ in range(num_edges):
        u, v, cost = input().split()
        cost = float(cost)
        nodes.update([u, v])
        graph.setdefault(u, []).append((v, cost))
        graph.setdefault(v, []).append((u, cost))  # For undirected graph

    print("\nEnter heuristic values for each node:")
    for node in nodes:
        h = float(input(f"Heuristic for node {node}: "))
        heuristics[node] = h

    return graph, heuristics

def main():
    graph, heuristics = build_graph()
    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    if start not in graph or goal not in graph:
        print("Start or goal node not found in the graph.")
        return

    path, cost = a_star_search(graph, heuristics, start, goal)
    if path:
        print(f"\nShortest path from {start} to {goal}: {' -> '.join(path)} with total cost {cost}")
    else:
        print(f"\nNo path found from {start} to {goal}.")

if __name__ == "__main__":
    main()