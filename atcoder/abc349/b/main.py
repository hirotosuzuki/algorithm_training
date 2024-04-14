#!/usr/bin/env python3

import collections

S = input()
S_list = list(S)
counter = collections.Counter(S_list)

d = {}
for k, v in counter.items():
  if d.get(v) is None:
    d[v] = 1
  else:
    d[v] += 1

for v in d.values():
  if v != 2:
    print("No")
    exit()

print("Yes")