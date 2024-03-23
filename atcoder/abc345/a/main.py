#!/usr/bin/env python3
S = input()

if S[0] != "<" or S[-1] != ">":
    print("No")
    exit()

for s in S[1: -1]:
    if s != "=":
        print("No")
        exit()

print("Yes")

