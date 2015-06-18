#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        prev = head
        current = head.next
        
        while current is not None:
            if current.val != prev.val:
                prev.next = current
                prev = current
            elif current.next is None and current.val == prev.val:
                prev.next = None
            
            current = current.next
        
        return head
