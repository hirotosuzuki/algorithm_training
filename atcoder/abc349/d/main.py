#!/usr/bin/env python3
L, R = map(int, input().split())

answers = [] # (left, right)のリスト

while L < R:
    i = 0
    # S(l, r) = S(pow(2, i)*j, pow(2, i)*(j+1))なので、
    # lがpow(2, i)で割り切れる かつ
    # rがl+pow(2, i)以下
    # を満たす最大のiが求める区間
    while (L % pow(2, i+1) == 0) and (L + pow(2, i+1) <= R):
        i += 1
    answers.append([L, L + pow(2, i)])
    L += pow(2, i)

print(len(answers))
for l, r in answers:
    print(l, r)
