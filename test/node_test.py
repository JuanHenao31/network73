from system73.entity.network import Network
from system73.entity.nodeofnetwork import NodeOfNetwork


class TestNodeClass:
    def test_serializer(self):
        my_node = NodeOfNetwork(key=2, capacity=1)

        serializer_resp = "Node " + str(my_node.key) + ":", {'key': my_node.key, 'capacity': my_node.capacity,
                                                             'availability': my_node.availability,
                                                             'parent_id': None,
                                                             'children_ids': []}
        assert my_node.serializer() == serializer_resp



