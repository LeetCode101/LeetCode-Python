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
            while current is not None and current.val == prev.val:
                current = current.next
            
            prev.next = current
            prev = current
        
        return head
