#!/usr/bin/env python3
S = input()

N = len(S)
datalake = set()
counter = 0
for i in range(N):
    for j in range(i, N):
        substring = S[i:j+1]
        datalake.add(substring)
print(len(datalake))