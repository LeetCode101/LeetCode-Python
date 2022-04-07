from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) \
            -> Optional[TreeNode]:
        nodes = {}
        parents = {}

        for parent, child, is_left in descriptions:
            child_node = TreeNode(child) if child not in nodes \
                else nodes[child]
            parent_node = TreeNode(parent) if parent not in nodes \
                else nodes[parent]

            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            if parent not in nodes:
                nodes[parent] = parent_node

            if child not in nodes:
                nodes[child] = child_node

            parents[child] = parent_node

        for key in nodes:
            if key not in parents:
                return nodes[key]
