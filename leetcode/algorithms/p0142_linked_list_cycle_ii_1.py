class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited, current = set(), head

        while current:
            if current.next and current.next in visited:
                return current.next
            else:
                visited.add(current)

            current = current.next

        return None
