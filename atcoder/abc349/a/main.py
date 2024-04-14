#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

# sum(A) + answer = 0
print(-sum(A))