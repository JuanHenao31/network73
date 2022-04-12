from system73.entity.nodeofnetwork import NodeOfNetwork
from system73.services.network_services.get_network import get_network
from system73.services.network_services.add_node import add_node
from system73.services.network_services.delete_node import delete_node

from system73.entity.network import Network

my_net = Network()
node_to_Delete = NodeOfNetwork(key=6, capacity=0)
my_net.add_node_network(NodeOfNetwork(key=1, capacity=2))
my_net.add_node_network(NodeOfNetwork(key=2, capacity=0))
my_net.add_node_network(NodeOfNetwork(key=3, capacity=0))
my_net.add_node_network(NodeOfNetwork(key=4, capacity=2))
my_net.add_node_network(NodeOfNetwork(key=5, capacity=1))
my_net.add_node_network(node_to_Delete)
my_net.add_node_network(NodeOfNetwork(key=7, capacity=4))
my_net.add_node_network(NodeOfNetwork(key=8, capacity=1))


def get_network_status():
    return get_network(my_net)


def add_node_network():
    return add_node(my_net)


def delete_node_network():
    return delete_node(my_net)
