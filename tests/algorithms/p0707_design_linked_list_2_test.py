import unittest
from leetcode.algorithms.p0707_design_linked_list_2 import MyLinkedList


class TestDesignLinkedList(unittest.TestCase):
    def test_design_linked_list(self):
        linked_list = MyLinkedList()
        linked_list.addAtHead(1)
        linked_list.addAtTail(3)
        linked_list.addAtIndex(1, 2)
        self.assertEqual(2, linked_list.get(1))

        linked_list.deleteAtIndex(1)
        self.assertEqual(3, linked_list.get(1))

        linked_list.addAtTail(2)
        self.assertEqual(2, linked_list.get(2))

        linked_list.deleteAtIndex(0)
        linked_list.deleteAtIndex(0)
        linked_list.deleteAtIndex(0)
        linked_list.addAtTail(1)
        self.assertEqual(1, linked_list.get(0))

        linked_list.addAtIndex(5, 5)
        linked_list.deleteAtIndex(0)
        linked_list.addAtIndex(0, 1)
        self.assertEqual(1, linked_list.get(0))

        linked_list.deleteAtIndex(5)
        linked_list.deleteAtIndex(0)
        self.assertEqual(-1, linked_list.get(0))

        linked_list.addAtHead(1)
        linked_list.addAtHead(2)
        self.assertEqual(1, linked_list.get(1))
