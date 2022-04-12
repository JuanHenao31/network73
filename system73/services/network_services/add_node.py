from flask import request, jsonify

from system73.controller.dto.node_dto import NodeDto
from system73.entity.network import Network
from system73.entity.nodeofnetwork import NodeOfNetwork


def add_node(actual_network: Network):
    data = request.get_json()
    node_dto = NodeDto(
        key=data['key'],
        capacity=data['capacity'],
        parent=None,
        children=[]
    )
    try:
        node = NodeOfNetwork(key=node_dto.key, capacity=node_dto.capacity)

        result = actual_network.add_node_network(my_new_node=node)

        return result, 200
    except:
        return jsonify({'message': 'Internal server error'}), 500
