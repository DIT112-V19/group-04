from math import sqrt, pow


class Map:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node, node2):
        edge = sqrt(pow(node2.x - node.x, 2)+pow(node2.y - node.y, 2))
        try:
            self.nodes[node][node2] = edge
        except KeyError:
            self.nodes[node] = {node2: edge}

        try:
            self.nodes[node2][node] = edge
        except KeyError:
            self.nodes[node2] = {node: edge}

    def add_one_way_node(self, node, node2):
        edge = sqrt(pow(node2.x - node.x, 2)+pow(node2.y - node.y, 2))
        try:
            self.nodes[node][node2] = edge
        except KeyError:
            self.nodes[node] = {node2: edge}
