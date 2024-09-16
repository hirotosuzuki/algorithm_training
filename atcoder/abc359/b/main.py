#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

answer = 0
for idx in range(0, 2 * N - 2):
    x = A[idx]
    y = A[idx + 2]
    if x == y:
        answer += 1
print(answer)
