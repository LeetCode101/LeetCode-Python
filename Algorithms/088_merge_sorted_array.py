#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        index_of_nums1 = m - 1
        index_of_nums2 = n - 1
        index_of_sorted_array = m + n - 1
        
        while index_of_nums1 >= 0 and index_of_nums2 >= 0:
            if nums1[index_of_nums1] < nums2[index_of_nums2]:
                nums1[index_of_sorted_array] = nums2[index_of_nums2]
                index_of_nums2 -= 1
            else:
                nums1[index_of_sorted_array] = nums1[index_of_nums1]
                index_of_nums1 -= 1
            
            index_of_sorted_array -= 1
        
        for i in range(index_of_nums1, -1, -1):
            nums1[index_of_sorted_array] = nums1[i]
            index_of_sorted_array -= 1
        
        for i in range(index_of_nums2, -1, -1):
            nums1[index_of_sorted_array] = nums2[i]
            index_of_sorted_array -= 1
