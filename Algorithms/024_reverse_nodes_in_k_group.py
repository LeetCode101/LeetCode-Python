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
        
        dummy = ListNode(0)    
        prev_group_head, prev_group_last= None, None
        
        while length >= k:
            length -= k
            prev_group_head, temp, head = self.reverse(head, k)
            
            if prev_group_last is not None:
                prev_group_last.next = prev_group_head
            
            prev_group_last = temp

            if dummy.next is None:
                dummy.next = prev_group_head
        
        if head is not None:
            prev_group_last.next = head
        
        return dummy.next
    
    def reverse(self, head, depth):
        dummy = ListNode(0)
        dummy.next = head
        prev, current, temp = None, head, None
        
        while current is not None and depth > 0:
            depth -= 1
            temp = current.next
            current.next = prev
            prev, current = current, temp
        
        return prev, dummy.next, current