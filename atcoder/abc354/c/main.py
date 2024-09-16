#!/usr/bin/env python3
N = int(input())
cards = []
for idx in range(N):
    a, c = map(int, input().split())
    cards.append((idx + 1, a, c))

# Attackで降順にする: O(N * logN)
cards.sort(key=lambda x: x[1], reverse=True)

answer = []
min_cost = 10 ** 9 + 1
for j in range(N):
    idx, a, c = cards[j]
    if min_cost > c:
        answer.append(idx)
        min_cost = c
answer.sort()
print(len(answer))
print(*answer, sep=" ")
