import random
import math

# Define coordinates for 10 cities
cities = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3),
    'F': (2, 7),
    'G': (3, 3),
    'H': (7, 8),
    'I': (9, 5),
    'J': (4, 9)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

def total_distance(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(path[i], path[(i + 1) % len(path)])
    return dist

def get_neighbors(path):
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climb(cities_list, iterations=1000):
    current_path = cities_list[:]
    random.shuffle(current_path)
    current_distance = total_distance(current_path)
    print(f"Initial path: {' -> '.join(current_path)} | Distance: {current_distance:.2f}")

    for i in range(iterations):
        neighbors = get_neighbors(current_path)
        next_path = min(neighbors, key=total_distance)
        next_distance = total_distance(next_path)

        if next_distance < current_distance:
            current_path = next_path
            current_distance = next_distance
            print(f"Iteration {i+1}: {' -> '.join(current_path)} | Distance: {current_distance:.2f}")
        else:
            print(f"Iteration {i+1}: No better neighbor found. Terminating.")
            break

    print(f"Final path: {' -> '.join(current_path)} | Distance: {current_distance:.2f}")
    return current_path, current_distance

if __name__ == "__main__":
    city_names = list(cities.keys())
    hill_climb(city_names, iterations=100)