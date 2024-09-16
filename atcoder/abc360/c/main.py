#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split())) # 荷物の初期位置
W = list(map(int, input().split())) # 荷物の重さ

# 全ての箱に荷物が一つずつ入っていて欲しい
# 荷物の移動にかかるコスト = 荷物の重さ
# 1つの箱に重複して入っている荷物の中で最も軽いものを選び、他の箱に移動させる

cost = 0

box = {i+1: [] for i in range(N)}
for a, w in zip(A, W):
    box[a].append(w)


for key, value in box.items():
    if len(value) > 1:
        # 最も重い荷物以外は他の箱に移動させる
        cost += sum(value) - max(value)

print(cost)
