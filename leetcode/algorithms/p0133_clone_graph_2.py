from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        visited = {}

        return self.clone(node, visited)

    def clone(self, node: Node, visited: Dict[Node, Node]) -> Node:
        if not node:
            return node

        if node not in visited:
            visited[node] = Node(node.val)
        else:
            return visited[node]

        for neighbor in node.neighbors:
            visited[node].neighbors.append(self.clone(neighbor, visited))

        return visited[node]
