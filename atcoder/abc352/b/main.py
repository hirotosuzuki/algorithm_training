#!/usr/bin/env python3
S = input()
T = input()

answer = []
i = 0
for s in S:
    if s in T[i:]:
        a = i + T[i:].index(s)
        answer.append(str(a + 1))
        i = a + 1

print(' '.join(answer))
