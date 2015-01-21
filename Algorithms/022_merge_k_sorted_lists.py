#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        length = len(lists)
        
        if length == 0:
            return None
            
        if length == 1:
            return lists[0]
            
        mid = (length - 1) >> 1
        
        left = self.mergeKLists(lists[0:mid + 1])
        right = self.mergeKLists(lists[mid + 1:])

        if left is None:
            return right
            
        if right is None:
            return left
        
        head, next, temp = None, None, None
        
        while left is not None and right is not None:
            if left.val < right.val:
                temp = left
                left = left.next
            else:
                temp = right
                right = right.next
                
            if head is None:
                head = temp
                next = temp
            else:
                next.next = temp
                next = next.next
                
        if left is not None:
            next.next = left
            
        if right is not None:
            next.next = right
            
        return head
