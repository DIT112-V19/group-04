import heapq
from utils import vector


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
    # Other types of heuristics can be possibly be used
    value = vector.Vector(node, goal).magnitude
    return value


def a_star_search(graph, start, goal):
    open_set = PriorityQueue()
    open_set.put(start, 0)
    closed_set = {}
    came_from = {}
    came_from[start] = None
    closed_set[start] = 0

    while not open_set.empty():
        current = open_set.get()

        if current == goal:
            break

        for child, weight in graph[current].items():
            cost = closed_set[current] + weight

            if child not in closed_set or cost < closed_set[child]:
                closed_set[child] = cost
                priority = cost + heuristic(child, goal)
                open_set.put(child, priority)
                came_from[child] = current

    return came_from, closed_set[goal]


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def run(graph, start, goal):
    came_from, cost = a_star_search(graph, start, goal)
    path = reconstruct_path(came_from, start, goal)
    return path, cost
