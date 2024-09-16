#!/usr/bin/env python3
N, T = map(int, input().split()) # N匹の蟻、T秒間
S = input() # 蟻の初期の向きを表す01の文字列
S = list(map(int, S))
X = list(map(int, input().split())) # 蟻の初期位置, 降順にソートされている, 初期位置が被ることはない

"""蟻Aと蟻Bがすれ違う条件
1. 向きが異なる
2. 0 < 左向き蟻の初期位置 - 右向き蟻の初期位置 <= 2 * T
"""

"""
全ての蟻の組み合わせに対して全探索すると N^2 = O(10^10)で間に合わない
ある範囲内にある蟻を探したい => しゃくとり法
"""
# answer = 0
# for idx in range(N):
#     x = X[idx]
#     s = S[idx]
#     if s == '1': # 右向き
#         for jdx in range(idx+1, N):
#             print(idx, jdx)
#             distance = X[jdx] - x
#             if distance > 2 * T:
#                 break
#             if S[jdx] == '0':
#                 answer += 1
# print(answer)
# X_right = [X[i] for i in range(len(S)) if S[i] == 1]
# X_left = [X[i] for i in range(len(S)) if S[i] == 0]
R = [0] * N # R[i]: i番目の蟻に対して条件を満たす and 最も遠くにいる左向き蟻のindex(i番目の蟻が左向きの場合は0)
A = [0] * N
k = 2 * T
for i in range(N):
    if i == 0:
        R[i] = 1
    else:
        R[i] = R[i-1]

    while R[i] < N and X[R[i]] - X[i] <= k:
        R[i] += 1

for i in range(N):
    # R[i] までの右向き蟻の数
    A[i] = R[i] - i - (len(S[i:R[i]]) - sum(S[i:R[i]]))

answer = sum([A[i] for i in range(len(S)) if S[i] == 1])
print(answer)
