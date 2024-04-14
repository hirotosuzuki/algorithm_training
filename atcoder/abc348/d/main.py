#!/usr/bin/env python3

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(input().split()[0]))
N = int(input())
RCE = {}
for _ in range(N):
    r, c, e = map(int, input().split())
    RCE[(r - 1, c - 1)] = e

# with open('./tests/sample-3.in', 'r') as f:
#     lines = f.readlines()

# # 1行目のデータを処理
# H, W = map(int, lines[0].split())

# # 2行目以降のデータを処理
# start = None
# goal = None
# A = []
# for line in lines[1:H+1]:
#     A.append(list(line.split()[0]))

# # 3行目以降のデータを処理
# N = int(lines[H+1])
# RCE = {}
# for line in lines[H+2:]:
#     r, c, e = map(int, line.split())
#     RCE[(r - 1, c - 1)] = e

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            start = (i, j)
        elif A[i][j] == 'T':
            goal = (i, j)

dp = [[-1 for _ in range(W)] for _ in range(H)]
dp[start[0]][start[1]] = RCE.get(start, 0)
if dp[start[0]][start[1]] == 0:
    print('No')
    exit()

for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a == '#':
            dp[i][j] = -1
            continue
        elif a == 'T' and dp[i][j] > 0:
            print('Yes')
            exit()

        # 4方向の最大値を取得
        up = dp[i-1][j] if i > 0 and A[i-1][j] != '#' else -1
        down = dp[i+1][j] if i < H - 1 and A[i+1][j] != '#' else -1
        left = dp[i][j-1] if j > 0 and A[i][j-1] != '#' else -1
        right = dp[i][j+1] if j < W - 1 and A[i][j+1] != '#' else -1

        dp[i][j] = max(
            dp[i][j],
            RCE.get((i, j), 0),
            up - 1,
            down - 1,
            left - 1,
            right - 1,
        )

if dp[goal[0]][goal[1]] >= 0:
    print('Yes')
else:
    print('No')

"""
[0,_3,_0,_0,_0]
[0,_2,_0,_0,_0]
[5,_0,_0,_0,_0]
[4,_3,_2,_1,_0]
"""