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
            
        length = 1
        current = head
        
        while current.next is not None:
            current = current.next
            length += 1
        
        current.next = head
        k = length - k % length
            
        while k > 0:
            current = current.next
            k -= 1
        
        head = current.next
        current.next = None
        
        return head
