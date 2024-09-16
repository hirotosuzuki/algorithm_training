#!/usr/bin/env python3
N, M = map(int, input().split())
H = list(map(int, input().split()))

remaining = M
for idx, h in enumerate(H):
    if remaining < h:
        print(idx)
        exit()
    remaining -= h

print(N)
