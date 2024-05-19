#!/usr/bin/env python3

H = int(input())
days = 0
tree = 0
while tree <= H:
    tree += 2**days
    days += 1

print(days)
