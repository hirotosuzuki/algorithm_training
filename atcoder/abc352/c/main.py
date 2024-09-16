#!/usr/bin/env python3

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_head_size = 0
max_head_index = 0
for idx, (a, b) in enumerate(zip(A, B)):
    if b - a > max_head_size:
        max_head_size = b - a
        max_head_index = idx

answer = 0
for idx, (a, b) in enumerate(zip(A, B)):
    if idx == max_head_index:
        continue
    answer += a

answer += B[max_head_index]

print(answer)
