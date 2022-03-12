
import functools

@functools.cache
def dynamic_programming(digit: int, number: int):
    if number == 1:
        return dynamic_programming(digit - 1, number) + dynamic_programming(digit - 1, number + 1)
    elif number == 9:
        return dynamic_programming(digit - 1, number) + dynamic_programming(digit - 1, number - 1)
    else:
        return dynamic_programming(digit - 1, number) + dynamic_programming(digit - 1, number) + dynamic_programming(digit - 1, number + 1)

class Task:
    def run(self):
        MOD = 998244353
        N = int(input())
        MAX_NUMBER = 8
        MIN_NUMBER = 0

        # dp[n][k]
        # 桁数n, 先頭の数字がkの時の条件を満たすXの個数
        # f(k, ?, ?) = f(k, k-1, ?) + f(k, k, ?) + f(k, k+1, ?)
        dp = [[0]*(MAX_NUMBER - MIN_NUMBER + 1) for _ in range(N)]

        for k in range(MAX_NUMBER+1):
            # 1桁で先頭がkの時、Xは1通り
            dp[0][k] = 1

        for n in range(1, N):
            # print("桁数n", n)
            for k in range(MAX_NUMBER+1):
                # print("先頭の数字k", k)
                # n桁で先頭がkの時のXの個数 = n-1桁で先頭がk-1 ~ k+1の時のXの個数
                # ただし、k-1>=1, k+1<=9
                for i in range(max(MIN_NUMBER, k-1), min(MAX_NUMBER, k+1)+1):
                    # print("i", i)
                    dp[n][k] += dp[n-1][i]
                    dp[n][k] %= MOD

        counter = 0
        for k in range(MAX_NUMBER+1):
            counter += dp[N-1][k]
            counter %= MOD

        print(counter)

    def run_2(self):
        MOD = 998244353
        N = int(input())
        print(dynamic_programming(N, ))



if __name__ == "__main__":
    task = Task()
    task.run()
