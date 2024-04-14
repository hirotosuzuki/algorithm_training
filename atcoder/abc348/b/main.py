#!/usr/bin/env python3
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

max_distance = [-1 for _ in range(N)]
max_points = [None for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        distance = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
        if distance > max_distance[i]:
            max_distance[i] = distance
            max_points[i] = j

for i in range(N):
    print(max_points[i] + 1)