#!/usr/bin/env python3
N = int(input())

answer = 0
for _ in range(N):
    name = input()
    if name == "Takahashi":
        answer += 1

print(answer)
