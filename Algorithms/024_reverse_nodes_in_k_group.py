#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        length, temp = 0, head
        
        while temp:
            length += 1
            temp = temp.next
        
        if length < k:
            return head
            
        prev_group_head, stack = None, []
        
        while length >= k:
            prev_group_head, head = self.reverse_list(head, k)
            stack.append(prev_group_head)
            length -= k
        
        if head is not None:
            stack.append(head)
        
        head = stack.pop(0)
        temp = head
        
        while len(stack) != 0:
            while temp.next is not None:
                temp = temp.next
            
            temp.next = stack.pop(0)
        
        return head
    
    def reverse_list(self, head, depth):
        prev, current, temp = None, head, None
        
        while current is not None and depth > 0:
            depth -= 1
            temp = current.next
            current.next = prev
            prev, current = current, temp
        
        return prev, current