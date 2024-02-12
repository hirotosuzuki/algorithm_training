#!/usr/bin/env python3
a, b, d = map(int, input().split())

# 等差数列の一般項 a_n = a_1 + (n-1)d
answer = [str(a)]
a_n = a
while a_n < b:
    a_n += d
    answer.append(str(a_n))
print(' '.join(answer))
