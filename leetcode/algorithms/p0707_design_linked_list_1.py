class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        i = 0
        current = self.head

        while current and i < index:
            current = current.next
            i += 1

        return current.value if current else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of
        the linked list.
        """
        new_head = Node(val)
        self.head, new_head.next = new_head, self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head

        while current and current.next:
            current = current.next

        if current:
            current.next = Node(val)
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        i = 0
        prev = None
        current = self.head

        while current and i < index:
            prev, current = current, current.next
            i += 1

        if i != index:
            return

        if prev:
            new_node = Node(val)
            prev.next, new_node.next = new_node, current
        else:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        prev = None
        current = self.head

        while current and i < index:
            prev, current = current, current.next
            i += 1

        if i != index:
            return

        if prev and current:
            prev.next, current.next = current.next, None
        elif current:
            current.next, self.head = None, current.next
