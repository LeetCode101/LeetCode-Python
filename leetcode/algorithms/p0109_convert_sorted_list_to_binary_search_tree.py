class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = self._get_sorted_array(head)

        return self._convert_sorted_array_to_bst(values, 0, len(values) - 1)

    def _get_sorted_array(self, head):
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values

    def _convert_sorted_array_to_bst(self, values, low, high):
        if low > high:
            return None

        middle = low + (high - low) // 2
        root = TreeNode(values[middle])
        root.left = self._convert_sorted_array_to_bst(
            values, low, middle - 1)
        root.right = self._convert_sorted_array_to_bst(
            values, middle + 1, high)

        return root
