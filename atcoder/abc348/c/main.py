#!/usr/bin/env python3
N = int(input())
AC = []
for _ in range(N):
    a, c = map(int, input().split())
    AC.append((a, c))

min_oishi= {}
for (a, c) in AC:
    min_oishi[c - 1] = min(min_oishi.get(c - 1, 10**10), a)

min_max = 0
for k, v in min_oishi.items():
    min_max = max(min_max, v)
print(min_max)