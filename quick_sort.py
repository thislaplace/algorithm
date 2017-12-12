#!/usr/bin/python3
# coding=utf-8

import time

# 这种写法虽然简单，但是缺陷也很明显

def quickSort(array):
    if len(array) < 2:
        return array
    less = [i for i in array[1:] if i <= array[0]]
    greater = [i for i in array[1:] if i > array[0]]
    print(less, greater)
    time.sleep(1)
    return quickSort(less) + [array[0]] + quickSort(greater)

print(quickSort([10, 12, 23, 12, 10, 2, 1, 4 ,5]))
