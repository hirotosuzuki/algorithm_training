#!/usr/bin/env python3
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

cost = abs(Ty - Sy) # y方向のコストは確定

if Sy == Ty:
    if Sy % 2 == 0:
        cost += Tx//2 - Sx//2
    else:
        cost += (Tx - 1)//2 - (Sx - 1)//2
    print(cost)
    exit()


x = abs(Tx - Sx)
y = abs(Ty - Sy)

if x <= y + 1:
    print(cost)
    exit()

cost += (x - y) // 2
print(cost)
