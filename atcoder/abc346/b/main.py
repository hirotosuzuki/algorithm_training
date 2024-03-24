#!/usr/bin/env python3
"""
abb abb abb abb
(0, 1): a: 1, b: 0
(0, 2): a: 1, b: 1
(0, 3): a: 1, b: 2
(0, 4): a: 2, b: 2
(0, 5): a: 2, b: 3
(0, 6): a: 2, b: 4
"""


B, W = map(int, input().split())
S = list("wbwbwwbwbwbwwbw") # W: 9, B: 6

patterns = []
for i in range(len(S)):
    for j in range(i+1, len(S)):
        substring = S[i:j]
        count_w = substring.count('w')
        count_b = substring.count('b')
        if count_w == W and count_b == B:
            print("Yes")
            exit()
        patterns.append((count_w, count_b))

for w, b in patterns:
    if (W - w) % 9 == 0 and (B - b) % 6 == 0:
        print("Yes")
        exit()


print("No")
