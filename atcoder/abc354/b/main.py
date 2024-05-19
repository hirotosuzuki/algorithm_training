#!/usr/bin/env python3
N = int(input())
data = []
c_sum = 0
for _ in range(N):
    s, c = input().split()
    c = int(c)
    c_sum += c
    data.append((s, c))

data.sort(key=lambda x: x[0])
print(data[c_sum % N][0])
