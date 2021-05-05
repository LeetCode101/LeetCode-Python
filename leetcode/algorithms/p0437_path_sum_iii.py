class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        sums = {0: 1}

        return self._dfs(root, 0, targetSum, sums)

    def _dfs(self, root, sum_so_far, target, sums):
        if not root:
            return 0

        sum_so_far += root.val
        count_ended_at_root = sums.get(sum_so_far - target, 0)
        sums[sum_so_far] = sums.get(sum_so_far, 0) + 1

        count_in_left = self._dfs(root.left, sum_so_far, target, sums)
        count_in_right = self._dfs(root.right, sum_so_far, target, sums)
        sums[sum_so_far] = sums[sum_so_far] - 1

        return count_ended_at_root + count_in_left + count_in_right
