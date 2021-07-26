# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
import math
import os
import random
import re
import sys


def maxSubarray(arr):
    # Subset
    arr1 = sorted(arr, reverse=True)
    subs = arr1[0]
    i = 1
    while i < len(arr1) and subs + arr1[i] > subs:
        subs += arr1[i]
        i += 1
    # Subarray
    MSS = [0]*len(arr)
    MSS[0] = arr[0]
    for i in range(1, len(arr)):
        MSS[i] = max(arr[i], MSS[i-1] + arr[i])

    return max(MSS)


if __name__ == '__main__':

    t = int(input("Enter :"))

    for i in range(t):
        n = int(input())

        arr = list(map(int, input()))

        result = maxSubarray(arr)

print(result, "is the answer.")
