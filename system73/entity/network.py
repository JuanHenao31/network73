from system73.entity.nodeofnetwork import NodeOfNetwork


class Network(object):
    def __init__(self):
        self.myNetwork: NodeOfNetwork = list()

    def add_node_network(self, my_new_node):
        if len(self.myNetwork) > 0:
            parent_node = self.node_mayor_availability()
            parent_node.add_child(my_new_node)

        self.myNetwork.append(my_new_node)

        return my_new_node.serializer()

    def remove_node_network(self, node):
        root_node = self.find_root_node(node)
        sub_tree = self.find_sub_tree(root_node)
        self.myNetwork = [x for x in self.myNetwork if x not in sub_tree]
        sub_tree.remove(node)
        self.reorder_tree(sub_tree)
        return "Node Eliminated"

    def find_root_node(self, node):
        if node.parent is None:
            return node
        else:
            return self.find_root_node(node.parent)

    def reorder_tree(self, nodes):
        nodes.sort(key=lambda x: x.capacity, reverse=True)

        for node in nodes:
            self.reset_node(node)

        self.add_node_network(nodes[0])
        nodes.pop(0)
        for node in nodes:
            parent_node = self.node_mayor_capacity()
            parent_node.add_child(node)
            self.myNetwork.append(node)

    def mayor_availability(self) -> int:
        list_of_availability = [num.availability for num in self.myNetwork]
        return max(list_of_availability)

    def mayor_capacity(self):
        list_of_capacities = [num.capacity for num in self.myNetwork if num.availability != 0]
        return max(list_of_capacities)

    def node_mayor_capacity(self):
        target = self.mayor_capacity()
        return self.search_node_capacity(target)

    def node_mayor_availability(self):
        target = self.mayor_availability()
        return self.search_node_availability(target)

    def search_node_availability(self, target):
        for node in self.myNetwork:
            if node.availability == target:
                return node
        return None

    def search_node_capacity(self, target):
        for node in self.myNetwork:
            if node.availability != 0 and node.capacity == target:
                return node
        return None

    @staticmethod
    def reset_node(node):
        node.parent = None
        node.children = []
        node.availability = node.capacity

    @staticmethod
    def find_sub_tree(root_node):

        # https://www.geeksforgeeks.org/sum-elements-n-ary-tree/
        sub_tree = list()
        if root_node is None:
            return sub_tree
        q = [root_node]

        while len(q) != 0:
            n = len(q)
            while n > 0:
                p = q[0]
                q.pop(0)
                sub_tree.append(p)
                for i in range(len(p.children)):
                    q.append(p.children[i])
                n -= 1
        return sub_tree
