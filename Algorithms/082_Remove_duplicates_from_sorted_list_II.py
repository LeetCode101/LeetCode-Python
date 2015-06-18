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
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current is not None:
            duplicate = False
            
            while current.next is not None and prev.next.val == current.next.val:
                current = current.next
                duplicate = True
            
            if not duplicate:
                prev = current
            else:
                prev.next = current.next
            
            current = current.next
        
        return dummy.next
