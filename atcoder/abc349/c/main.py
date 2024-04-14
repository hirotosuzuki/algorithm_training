#!/usr/bin/env python3
S = input() # haneda
T = input() # HND

if T[-1] == 'X':
    T = T[:-1]

search_idx = 0
for t in T:
    t_lower = t.lower()
    if t_lower not in S[search_idx:]:
        print("No")
        exit()
    search_idx = S.index(t_lower, search_idx) + 1
print("Yes")