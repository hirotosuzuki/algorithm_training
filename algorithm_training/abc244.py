class TaskA:
    def run(self):
        V, A, B, C = map(int, input().split())
        pass
import numpy as np

class Point:
    def __init__(self) -> None:
        self.p = np.array([0, 0])
        self.direction = np.array([1, 0])
        theta = np.radians(-90)
        self.rotation_matrix = np.array(
            [
                [np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]
            ]
        )

    def rotate(self) -> None:
        self.direction = np.round(
            np.dot(
                self.rotation_matrix,
                self.direction.T,
            )
        ).astype(int)

    def update(self) -> None:
        self.p = (self.p + self.direction).astype(int)

class TaskB:
    def run(self):
        N = int(input())
        T = input()
        p = Point()
        for t in T:
            if t == "S":
                p.update()
            else:
                p.rotate()
        print(p.p[0], p.p[1])

import sys

class TaskC:
    def run(self):
        N = int(input())
        number_set = set([i for i in range(1, 2*N+1+1)])
        while True:
            print(number_set.pop())
            n = int(input())
            if n == 0:
                sys.exit()
            number_set.remove(n)

class TaskD:
    def run(self):
        S = input().split() # ["R", "G", "B"]
        T = input().split()

        if S[0] == T[0]:
            if S[1] == T[1]:
                if S[2] == T[2]:
                    # 3人同じ
                    print("Yes")
                else:
                    # 2人同じ
                    print("No")
            else:
                if S[2] == T[2]:
                    # 2人同じ
                    print("No")
                else:
                    # 1人同じ
                    print("No")
        else:
            if S[1] == T[1]:
                if S[2] == T[2]:
                    # 2人同じ
                    print("No")
                else:
                    # 1人同じ
                    print("No")
            else:
                if S[2] == T[2]:
                    # 1人同じ
                    print("No")
                else:
                    # 0人同じ
                    print("Yes")

class TaskE:
    def run(self):
        MOD = 998244353
        N, M, K, S, T, X = map(int, input().split())
        # 頂点番号は0始まりにする
        S -= 1
        T -= 1
        X -= 1

        edge = []
        for i in range(M):
            U, V = map(int, input().split())
            # 頂点番号は0始まりにする
            U -= 1
            V -= 1
            edge.append((U, V))

        # dp[x][k][t]: 頂点Sから辺をk回通って頂点tへ行き、途中で頂点Xを通った回数 mod 2 がxである経路の数
        # 求めたい： dp[0][K][T]
        # 漸化式：dp[x][k+1][t] = sum(dp[x][k][t]) (t != Xの時)
        dp = [
            [
                [0] * N for i in range(K + 1)
            ] for x in range(2)
        ]

        # 初期状態
        # dp[x][k][t]: 頂点Sから頂点Sへ、辺を0回通って行き、頂点Xを通った回数が偶数(0回)であるのは1通り
        # スタート地点Sにいるので頂点Xは通ってないから
        dp[0][0][S] = 1

        for k in range(K): # パス長: k
            for U, V in edge: # 全ての辺
                for x in range(2): # 頂点Xを通った回数の偶奇
                    # x ^ (V == X): 終点Vが頂点Xの時、偶奇が反転する
                    # 頂点Sから頂点Vへ、k+1パスで行き、頂点Xを通った回数の偶奇がxであるのは、
                    # 頂点Sから頂点Uへ、kパスで行き、その次にU -> Vへ行った時に、
                    # VがX かつ Uまでの偶奇が偶数 -> Vまでの偶奇は奇数
                    dp[x][k + 1][V] += dp[x ^ (V == X)][k][U]
                    if dp[x][k + 1][V] >= MOD:
                        dp[x][k + 1][V] -= MOD

                    dp[x][k + 1][U] += dp[x ^ (U == X)][k][V]
                    if dp[x][k + 1][U] >= MOD:
                        dp[x][k + 1][U] -= MOD
        print(dp[0][K][T])

if __name__ == "__main__":
    task = TaskE()
    task.run()