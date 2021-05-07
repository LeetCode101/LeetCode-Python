from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) \
            -> TreeNode:
        stack = [TreeNode(pre[0])]
        j = 0

        for value in pre[1:]:
            node = TreeNode(value)

            while stack[-1].val == post[j]:
                stack.pop()
                j += 1

            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]
