#!/usr/bin/env python3


S, T = input().split()

for w in range(1, len(S)):
    # Sをw文字ずつに区切る
    words = [S[i:i+w] for i in range(0, len(S), w)]

    # 長さが c 以上の文字列の c 文字目を順番に連結した文字列
    for c in range(1, w + 1):
        result = ''
        for word in words:
            if len(word) >= c:
                result += word[c - 1]
        if result == T:
            print('Yes')
            exit()

print('No')

