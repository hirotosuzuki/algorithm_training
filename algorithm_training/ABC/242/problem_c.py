pattern = {
    1: 2,
    2: 3,
    3: 3,
    4: 3,
    5: 3,
    6: 3,
    7: 3,
    8: 3,
    9: 2,
}

class Task:
    def run(self):
        # N, M = map(int, input().split())
        # print(N + M)
        divider = 998244353
        N = int(input())
        counter = 0
        for X in range(10**(N-1) + 1, 10**N):
            X = str(X)
            if "0" in X:
                continue

            num_x = len(X)

            # 123
            # (1, 2), (2, 3)
            ok_list = []
            for i in range(num_x):
                X_i = int(X[i])
                for j in range(num_x):
                    X_j = int(X[j])
                    if i != j - 1:
                        continue
                    if abs(X_i - X_j) <= 1:
                        ok_list.append(1)
                    else:
                        ok_list.append(0)
            if min(ok_list)>0:
                counter += 1

        if counter < divider:
            print(counter)
        else:
            print(counter % divider)





if __name__ == "__main__":
    task = Task()
    task.run()
