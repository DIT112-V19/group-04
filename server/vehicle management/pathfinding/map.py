import vector


class Map:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node, node2):
        edge = vector.Vector(node.position, node2.position).magnitude
        try:
            self.nodes[node][node2] = edge
        except KeyError:
            self.nodes[node] = {node2: edge}

        try:
            self.nodes[node2][node] = edge
        except KeyError:
            self.nodes[node2] = {node: edge}
