#!/usr/bin/env python3
from fractions import Fraction


N, K = map(int, input().split())
A = set()
for a in map(int, input().split()):
    if a <= K:
        A.add(a)


# 1からKまでの総和 = K*(K-1)/2
K_sum = int(Fraction(K*(K+1), 2))
answer = K_sum - sum(A)
print(answer)