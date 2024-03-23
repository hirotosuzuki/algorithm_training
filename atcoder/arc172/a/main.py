#!/usr/bin/env python3

H, W, N = map(int, input().split())
A = list(map(int, input().split()))

# 配るチョコの総数 > H x Nの場合はNo
need_num = 0
for a in A:
    need_num += 2**(2 * a)
if need_num > H * W:
    print('No')
    exit()

# 辺の長さを超過する場合は、そのチョコは配ることができない
def is_possible(h, w, a) -> bool:
    if len(a) == 0:
        return True
    if min(h, w) < 2 ** max(a):
        return False
    a_max = a.pop(0)
    return is_possible(h - 2 ** a_max, w, a) or is_possible(h, w - 2 ** a_max, a)

sorted_A = sorted(A, reverse=True)
x = is_possible(H, W, sorted_A)
if x:
    print('Yes')
else:
    print('No')
