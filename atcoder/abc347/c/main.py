#!/usr/bin/env python3
N, A, B = map(int, input().split())
D = list(map(int, input().split()))
MOD = A + B
D = [d % MOD for d in D]
d_max = max(D)
d_min = min(D)
diff = d_max - d_min
if diff > A:
    print("No")
else:
    print("Yes")
