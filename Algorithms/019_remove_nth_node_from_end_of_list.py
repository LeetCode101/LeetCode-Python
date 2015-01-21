#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        count = 0
        temp = head
        
        while temp is not None:
            count += 1
            temp = temp.next
            
        if count == n:
            return head.next
            
        i = 1
        temp, prev = head, None
        
        while temp is not None:
            if i == count - n + 1:
                prev.next = temp.next
                return head
            
            i += 1
            prev = temp
            temp = temp.next
