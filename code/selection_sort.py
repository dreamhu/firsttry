#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 时间复杂度O(n2)

def find_smallest(nums):
	smallest = nums[0]
	smallest_idx = 0
	for idx in xrange(len(nums)):
		if nums[idx] < smallest:
			smallest = nums[idx]
			smallest_idx = idx

	return smallest_idx


def selection_sort(nums):
	sorted_nums = []
	for idx in xrange(len(nums)):
		# 每次都传入剩下的数组查找最新的数
		smallest_idx = find_smallest(nums)
		sorted_nums.append(nums.pop(smallest_idx))
	return sorted_nums

print selection_sort([5, 3, 6, 2, 10])