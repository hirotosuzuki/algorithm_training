#!/usr/bin/env python3
L, R = map(int, input().split())


def s_func(l, r, counter=0):
    if l % 2 == 1:
        counter += 1
        s_func(l+1, r, counter)
    else:
        # lが偶数のとき、rが2の何乗かでiが決まる
        pass