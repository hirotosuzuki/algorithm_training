#!/usr/bin/env python3

N, H, W = map(int, input().split())
tiles = []
total_area = 0
min_a = 100
min_b = 100
for _ in range(N):
    a, b = map(int, input().split())
    tiles.append((a, b))
    total_area += a * b
    if a < min_a:
        min_a = a
    if b < min_b:
        min_b = b

if total_area < H * W:
    print("No")
    exit()

if min_a >= H or min_b >= W:
    print("No")
    exit()


print("Yes")

