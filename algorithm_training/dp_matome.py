class TaskA_Frog1:
    # https://atcoder.jp/contests/dp/tasks/dp_a
    def run(self):
        N = int(input())
        H = list(map(int, input().split()))

        dp = [0] * N
        # 0 ~ N-1の足場とする
        dp[0] = 0
        dp[1] = abs(H[1] - H[0])

        for n in range(2, N):
            dp[n] = min(
                dp[n - 1] + abs(H[n] - H[n - 1]),
                dp[n - 2] + abs(H[n] - H[n - 2])
            )

        print(dp[N - 1])


class TaskB_Frog2:
    # https://atcoder.jp/contests/dp/tasks/dp_b
    def run(self):
        import sys
        from functools import cache
        input = sys.stdin.readline

        N, K = map(int, input().split())
        H = list(map(int, input().split()))


        dp = [0] * N
        # 0 ~ N-1の足場とする
        dp[0] = 0
        dp[1] = abs(H[1] - H[0])

        for n in range(2, N):
            min_cost = 10000000000
            for k in range(1, K + 1): # k = 1 ~ K
                if n - k >= 0:
                    if (cost:= abs(H[n] - H[n - k]) + dp[n - k]) < min_cost:
                        min_cost = cost
            dp[n] = min_cost

        print(dp[N - 1])

class TaskC_Vacation:
    # https://atcoder.jp/contests/dp/tasks/dp_c
    def run(self):
        import sys
        input = sys.stdin.readline

        N = int(input())
        ABC = [list(map(int, input().split())) for _ in range(N)]

        # DPテーブルの宣言・初期化
        dp = [[0]*3 for _ in range(N)]
        dp[0] = ABC[0]

        # 漸化式
        for i in range(1, N): # 1 ~ N-1
            # i日目に行動Aをした時の最大幸福度
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + ABC[i][0]
            # i日目に行動Bをした時の最大幸福度
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + ABC[i][1]
            # i日目に行動Cをした時の最大幸福度
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][0]) + ABC[i][2]

        print(max(dp[N - 1]))

if __name__ == "__main__":
    TaskC_Vacation().run()