#!/usr/bin/env python3
N = int(input())
print("".join(["o" if i % 3 !=0 else "x" for i in range(1, N+1)]))