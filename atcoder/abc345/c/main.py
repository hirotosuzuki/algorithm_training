#!/usr/bin/env python3

from math import factorial

def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

S = input()
N = len(S)
dataset = dict()
for s in S:
    if dataset.get(s) is not None:
        dataset[s] += 1
        continue
    dataset[s] = 1

counter = 0
for v in dataset.values():
    counter += v * (N - v)

if max(dataset.values()) == 1:
    print(counter // 2)
    exit()
else:
    print(counter // 2 + 1)