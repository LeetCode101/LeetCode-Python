class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited, current = set(), head

        while current is not None:
            if current.next is not None and current.next in visited:
                return True
            else:
                visited.add(current)

            current = current.next

        return False
