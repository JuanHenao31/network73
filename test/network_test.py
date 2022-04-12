from system73.entity.network import Network
from system73.entity.nodeofnetwork import NodeOfNetwork
from unittest.mock import patch, MagicMock


class TestNetworkClass:

    def test_add_node_network(self):
        my_net = Network()
        parent_node = NodeOfNetwork(key=1, capacity=1)
        child_node = NodeOfNetwork(key=2, capacity=1)

        my_net.add_node_network(parent_node)
        my_net.add_node_network(child_node)

        assert child_node.parent.key == parent_node.key
        assert len(parent_node.children) > 0
        assert child_node.key == parent_node.children[0].key
        assert parent_node.parent is None

    @patch.object(Network, 'find_root_node')
    @patch.object(Network, 'find_sub_tree')
    @patch.object(Network, 'reorder_tree')
    def test_remove_node_network(self, find_root_node, find_sub_tree, reorder_tree):
        my_net = Network()
        parent_node = NodeOfNetwork(key=1, capacity=1)
        child_node = NodeOfNetwork(key=2, capacity=1)

        my_net.reorder_tree = MagicMock()

        my_net.add_node_network(parent_node)
        my_net.add_node_network(child_node)

        find_root_node.return_value = parent_node
        find_sub_tree.return_value = [parent_node, child_node]

        my_net.remove_node_network(child_node)

        assert my_net.reorder_tree.called
        assert find_sub_tree.called

