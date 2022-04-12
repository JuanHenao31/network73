from flask import jsonify

from system73.entity.network import Network
import json


def get_network(actual_network: Network):
    answer = []
    for i in actual_network.myNetwork:
        answer.append(i.serializer())
    return answer
