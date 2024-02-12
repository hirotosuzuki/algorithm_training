#!/usr/bin/env python3

Q = int(input())
A = []
for _ in range(Q):
    n, m = map(int, input().split())
    if n == 1:
        A.append(m)
    else:
        print(A[-m])