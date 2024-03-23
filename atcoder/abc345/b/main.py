#!/usr/bin/env python3

X = int(input())
a = X // 10
b = X % 10
if b == 0:
    print(a)
else:
    print(a + 1)