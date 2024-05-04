#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, []

    mid = len(arr) // 2
    left_half, left_swaps = merge_sort(arr[:mid])
    right_half, right_swaps = merge_sort(arr[mid:])
    merged, merge_swaps = merge(left_half, right_half)
    total_swaps = left_swaps + right_swaps + merge_swaps
    return merged, total_swaps

def merge(left, right):
    merged = []
    swaps = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            for k in reversed(left[i:]):
                swaps.append([right[j], k])
            merged.append(right[j])
            j += 1


    if i < len(left):
        merged.extend(left[i:])

    if j < len(right):
        merged.extend(right[j:])

    return merged, swaps

merged, answer = merge_sort(A)

print(len(answer))
for a in answer:
    if a[0] <= a[1]:
        print(a[0], a[1])
    else:
        print(a[1], a[0])
