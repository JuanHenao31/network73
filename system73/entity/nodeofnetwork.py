class NodeOfNetwork(object):

    def __init__(self, key: int, capacity=0, parent=None):
        self.key = key
        self.parent: NodeOfNetwork = None
        self.children = list()
        self.capacity = capacity
        self.availability = capacity

        self.set_parent(parent)

    def set_parent(self, parent):
        if parent and self.parent is not parent and parent.availability != 0:
            self.parent = parent
        else:
            self.parent = None

    def add_child(self, node):
        if len(self.children) <= self.availability:
            node.set_parent(self)
            self.availability = self.availability - 1
            self.children.append(node)

    def serializer(self):

        return "Node " + str(self.key) + ":", {'key': self.key, 'capacity': self.capacity,
                                               'availability': self.availability,
                                               'parent_id': self.parent.key if self.parent is not None else None,
                                               'children_ids': [child.key for child in self.children if
                                                                child is not None]}
