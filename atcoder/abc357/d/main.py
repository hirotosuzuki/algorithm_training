#!/usr/bin/env python3
N = int(input())
digit = len(str(N))
MOD = 998244353

# 逆元を計算する関数
# フェルマーの小定理より、aの逆元はa^(MOD-2)で求められる
def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

# 高速べき乗法を用いて、a^n mod mを計算する関数
def modular_exponentiation(a, n, m):
    result = 1  # 初期値を1に設定
    a = a % m  # 最初の数をmで割った余りに変換

    while n > 0:
        # nが奇数の場合
        if (n % 2) == 1:
            result = (result * a) % m

        # nを半分にする
        n = n >> 1  # nを2で割る
        a = (a * a) % m  # aを2乗した値をmで割った余りに変換

    return result

if N < 9:
    print(str(N)*N)
    exit()

# Vn = N * ((10**(N*digit)) - 1) /  (10**digit - 1)

inverse = mod_inverse(10**digit - 1, MOD)
numerator = modular_exponentiation(10, N*digit, MOD)
numerator = (numerator - 1) % MOD
numerator = (N * numerator) % MOD
answer = (numerator * inverse) % MOD
print(answer)
