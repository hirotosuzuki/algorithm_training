#!/usr/bin/env python3

N, Q = map(int, input().split())
T = list(map(int, input().split()))

# N: 穴の数
# Q: クエリの数
# T: 歯の配列

teeth = [1] * N

for t in T:
    x = teeth[t-1]
    if x == 0:
        teeth[t-1] = 1
    else:
        teeth[t-1] = 0

print(sum(teeth))
