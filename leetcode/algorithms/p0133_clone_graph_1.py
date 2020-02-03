from collections import deque


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node

        queue = deque([node])
        visited = {
            node: Node(node.val)
        }

        while queue:
            old_node = queue.popleft()

            for neighbor in old_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[old_node].neighbors.append(visited[neighbor])

        return visited[node]
