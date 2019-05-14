import math


def node_finder(graph,x, y):
    distance = math.inf
    found_node = None
    for node in graph:
        new_distance = math.pow(node.x-x, 2)+math.pow(node.y-y, 2)
        if new_distance < distance:
            distance = new_distance
            found_node = node
    return found_node
