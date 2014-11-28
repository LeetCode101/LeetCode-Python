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
        remain = ListNode(0)
        new = ListNode(self.calculate_node_value(remain, l1, l2))
        head = new
        l1, l2 = l1.next, l2.next
        
        while l1 and l2:
            next = ListNode(self.calculate_node_value(remain, l1, l2))
            new.next = next
            new = next
            l1, l2 = l1.next, l2.next
            
        while l1:
            next = ListNode(self.calculate_node_value(remain, l1))
            new.next = next
            new = next
            l1 = l1.next
            
        while l2:
            next = ListNode(self.calculate_node_value(remain, l2))
            new.next = next
            new = next
            l2 = l2.next
            
        if remain.val != 0:
            next = ListNode(remain.val)
            new.next = next
            new = next
        
        return head
    
    def calculate_node_value(self, remain, *nodes):
        total = 0
        
        for node in nodes:
            total += node.val
            
        total += remain.val
        
        remain.val = total / 10
            
        return total % 10