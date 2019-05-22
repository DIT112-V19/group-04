import heapq
from math import pow, sqrt


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(node, goal):
    # Other types of heuristics can be possibly be used.
    # For now it seems euclidean distance is the best option.
    value = sqrt(pow(goal.x - node.x, 2)+pow(goal.y - node.y, 2))
    return value


def a_star_search(graph, start, goal):
    # Open set will be the vertices that haven't yet been checked, in a* this begins empty
    open_set = PriorityQueue()
    # Begin finding the path from the start.
    open_set.put(start, 0)
    # Closed set are the vertices that have been checked.
    closed_set = {}
    came_from = {}
    # As start is the first point this means it didn't come from anywhere.
    came_from[start] = None
    # It doesn't cost anything to go to start from start.
    closed_set[start] = 0

    while not open_set.empty():
        current = open_set.get()

        if current == goal:
            break

        for child, weight in graph[current].items():
            cost = closed_set[current] + weight

            if child not in closed_set or cost < closed_set[child]:
                closed_set[child] = cost
                # The priority of checking a vertex is the weight + heuristic i.e. F=G+H.
                priority = cost + heuristic(child, goal)
                open_set.put(child, priority)
                came_from[child] = current

    return came_from, closed_set[goal]


def reconstruct_path(came_from, start, goal):
    # This reconstructs the path from the end to the beginning.
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    # So the path must be reversed.
    path.reverse()
    return path


def run(graph, start, goal):
    came_from, cost = a_star_search(graph, start, goal)
    path = reconstruct_path(came_from, start, goal)
    return path, cost
