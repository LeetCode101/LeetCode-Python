#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        node, head = None, None
        remain = ListNode(0)
        
        while l1 is not None or l2 is not None:
            total = 0
            
            if l1 is not None:
                total += l1.val
                l1 = l1.next
                
            if l2 is not None:
                total += l2.val
                l2 = l2.next
                
            total += remain.val
            remain.val = total / 10
            
            if node is not None:
                node.next = ListNode(total % 10)
                node = node.next
            else:
                node = ListNode(total % 10)
                
            if head is None:
                head = node
            
        if remain.val == 1:
            node.next = ListNode(1)
        
        return head
