#!/usr/bin/env python3

S = input()

if S == "ABC316":
    print("No")
    exit()

number = int(S[-3:])
if 1 <= number <= 349:
    print("Yes")
else:
    print("No")
