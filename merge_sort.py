#!/usr/bin/python
# coding = utf-8

import time

array = [12, 23, 21, 2, 45, 4, 10]

def mergeArr(arrLeft, arrRight):
    arr = []
    i, k = 0, 0

    while (i < len(arrLeft) and k < len(arrRight)):
        if arrLeft[i] < arrRight[k]:
            arr.append(arrLeft[i])
            i += 1
        else:
            arr.append(arrRight[k])
            k += 1

    if i == len(arrLeft)-1:
        arr.extend(arrLeft[i:])
    else:
        arr.extend(arrRight[k:])

    print(arr)
    time.sleep(1)
    return arr


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    return mergeArr(mergeSort(arr[0:len(arr)//2]), mergeSort(arr[len(arr)//2:]))

print(mergeSort(array))
