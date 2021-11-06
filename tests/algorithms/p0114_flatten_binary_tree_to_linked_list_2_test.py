import unittest
from leetcode.algorithms.p0114_flatten_binary_tree_to_linked_list_2 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import preorder


class TestFlattenBinaryTreeToLinkedList(unittest.TestCase):
    def test_flatten_binary_tree_to_linked_list(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(5, None, TreeNode(6))
        )

        solution.flatten(None)
        solution.flatten(root1)

        self.assertListEqual([1, 2, 3, 4, 5, 6], preorder(root1))
