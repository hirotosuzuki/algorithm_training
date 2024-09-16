#!/usr/bin/env python3

S = input()
# len(S)は奇数

lower_num = 0

for s in S:
    if s.islower():
        lower_num += 1

upper_num = len(S) - lower_num

if lower_num < upper_num:
    print(S.upper())
else:
    print(S.lower())
