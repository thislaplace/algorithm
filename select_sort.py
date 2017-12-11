#!/usr/bin/python3
# coding=utf-8
def findSmallest(arr, start):
    smallest = arr[start]
    index = start
    for i in range(start+1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            index = i
    return index

def selectionSort(arr):
    for i in range(len(arr)):
        smallest = findSmallest(arr, i)
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

print("输入你想排序的数字，中间用空格隔开, 回车键结束输入。")
arr = input().split()
#print(str)
print(selectionSort(arr))
