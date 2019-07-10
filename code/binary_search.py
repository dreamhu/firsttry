#!/usr/bin/python
# -*- coding: utf-8 -*-
# 时间复杂度O(logn)


def binary_search(sorted_nums, num):
    # 以数组下标为低位和高位索引
    low_pos = 0
    high_pos = len(sorted_nums) - 1

    # 低位和高位相等也要处理
    while low_pos <= high_pos:
        cur_pos = (low_pos + high_pos) / 2
        if sorted_nums[cur_pos] == num:
            return cur_pos
        elif sorted_nums[cur_pos] < num:
            # cur_pos已经匹配，需要多移一位
            low_pos = cur_pos + 1
        else:
            high_pos = cur_pos - 1
    return -1

print binary_search([1,2,3,4], 4)
