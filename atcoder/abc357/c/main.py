#!/usr/bin/env python3
N = int(input())

black = "#"
white = "."


def array_to_string(a):
    # 各行を文字列に変換し、行ごとに改行を追加
    result = "\n".join("".join(row) for row in a)
    return result

def level_k(k: int):
    # print(f"k: {k}")
    if k == 0:
        return [[black]]
    if k == 1:
        return [
            [black, black, black],
            [black, white, black],
            [black, black, black]
        ]

    k_1 = 3 ** (k - 1)
    k_2 = 3 ** (k - 1) * 2
    k_3 = 3 ** k
    carpet = [["o" for _ in range(k_3)] for _ in range(k_3)]

    # 中央の白い部分は 3**(k-1) x 3**(k-1) の白のマスである
    for i in range(k_1, k_2):
        for j in range(k_1, k_2):
            carpet[i][j] = white

    # 残りの部分は k-1 のレベルのカーペットで埋める
    before = level_k(k-1)

    for i in range(k_1):
        carpet[i] = before[i] * 3

    for i in range(k_2, k_3):
        carpet[i] = before[i - k_2] * 3

    for j in range(0, k_1):
        for i in range(k_1, k_2):
            carpet[i][j] = before[i-k_1][j]

    for i in range(k_1, k_2):
        for j in range(k_2, k_3):
            carpet[i][j] = before[i-k_1][j-k_2]
    return carpet

carpet = level_k(N)
print(array_to_string(carpet))
