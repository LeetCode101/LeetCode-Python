#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
            
        length = 0
        current = head
        last = None
        
        while current is not None:
            if current.next is None:
                last = current
                
            current = current.next
            length += 1
        
        if k % length == 0:
            return head
            
        depth = length - k % length
        current = head
        prev = None
        
        while depth > 0:
            prev = current
            current = current.next
            depth -= 1
        
        prev.next = None
        last.next = head
        
        return current
