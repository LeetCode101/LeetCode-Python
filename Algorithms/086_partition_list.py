#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        less_than_target = ListNode(0)
        greater_than_or_equal_to_target = ListNode(0)
        head1 = less_than_target
        head2 = greater_than_or_equal_to_target
        current = head
        
        while current is not None:
            if current.val < x:
                head1.next = current
                head1 = head1.next
            else:
                head2.next = current
                head2 = head2.next
                
            current = current.next
        
        head2.next = None
        head1.next = greater_than_or_equal_to_target.next
        
        return less_than_target.next
