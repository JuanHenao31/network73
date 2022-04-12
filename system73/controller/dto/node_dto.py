from dataclasses import dataclass

from system73.entity.nodeofnetwork import NodeOfNetwork


@dataclass
class NodeDto(object):
    key: int
    parent: NodeOfNetwork
    children: list()
    capacity: int
