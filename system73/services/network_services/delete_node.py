from flask import request, jsonify
import json

from system73.controller.dto.node_dto import NodeDto
from system73.entity.network import Network
from system73.entity.nodeofnetwork import NodeOfNetwork


def find_node(key, actual_network: Network):
    for node in actual_network.myNetwork:
        if node.key == key:
            return node
    raise Exception("Node Not Found")


def delete_node(actual_network: Network):
    data = request.get_json()
    node_dto = NodeDto(
        key=data['key'],
        capacity=None,
        parent=None,
        children=[]
    )
    try:
        node = find_node(node_dto.key, actual_network)

        result = actual_network.remove_node_network(node=node)

        return{'message': str(result)}, 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
