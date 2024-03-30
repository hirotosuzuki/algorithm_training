#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = [a // K for a in A if a % K == 0]
print(" ".join(map(str, answer)))