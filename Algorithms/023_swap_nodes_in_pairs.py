#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev, current, next = dummy, head, head.next
        
        while prev is not None and current is not None and next is not None:
            # Swap
            prev.next = next
            current.next, next.next = next.next, current

            prev = current
            current = prev.next

            if current is not None:
                next = current.next
            
        return dummy.next
