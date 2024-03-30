#!/usr/bin/env python3
N, A, B = map(int, input().split())
# A: 入れ替えコスト
# B: 置き換えコスト
S = input() # 長さ2Nの文字列

# 正しい括弧列
# 条件１：(の数と)の数が等しい
# 条件２：一番右にある「(」の位置 < 一番左にある「)」の位置

# 正しい括弧列にする最小コスト
# 条件1のコストは操作の仕方によらず変わらない => 個数の差分 x Bのコストは必ずかかる
# 条件2のコストは操作の仕方によって変わる => 入れ替えが必要な括弧を優先的に置き換える & 最短で入れ替える
