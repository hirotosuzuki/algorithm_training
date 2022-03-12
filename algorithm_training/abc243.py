from operator import index


class TaskA:
    def run(self):
        V, A, B, C = map(int, input().split())
        ABC = A + B + C
        V %= ABC
        if V < A:
            print("F")
        elif V - A < B:
            print("M")
        elif V - A - B < C:
            print("T")

class TaskB:
    def run(self):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        num_ai_equal_bi = 0
        for a, b in zip(A, B):
            if a == b:
                num_ai_equal_bi += 1
        num_ai_not_equal_bi = len(set(A) & set(B)) - num_ai_equal_bi
        print(num_ai_equal_bi)
        print(num_ai_not_equal_bi)

class TaskC:
    def run(self):
        answer = "No"
        import operator

        N = int(input())
        # XY = [[2, 3], [2, 1], ..]
        XY = [list(map(int, input().split())) for l in range(N)]
        # S = ["R", "L", "R", "R", ..]
        S = list(input())
        # XYS = [[2, 3, "R"], ...]
        XYS = [(xy[0], xy[1], s) for xy, s in zip(XY, S)]

        same_y_dict = dict()
        for x, y, s in XYS:
            if not same_y_dict.get(y):
                same_y_dict[y] = []
            same_y_dict[y].append((x, y, s))

        for points in same_y_dict.values():
            # 同一y上に２人以上いないと衝突しない
            if len(points) < 2:
                continue
            # X座標で並び替え
            points_sorted_by_x = sorted(points, key=operator.itemgetter(0))
            while len(points_sorted_by_x) > 1:
                min_x, min_x_direction, _ = points_sorted_by_x.pop(0)
                if min_x_direction == "L":
                    continue
                else:
                    # 他の点の向きが全てR
                    if not "L" in [s for x, y, s in points_sorted_by_x]:
                        continue
                    else:
                        answer = "Yes"

        print(answer)

class TaskAnswerC:
    def run(self):
        def Yes():
            print("Yes")
            exit(0)

        N = int(input())
        # XY = [[2, 3], [2, 1], ..]
        XY = [list(map(int, input().split())) for l in range(N)]
        # S = ["R", "L", "R", "R", ..]
        S = input()
        # XYS = [[2, 3, "R"], ...]
        XYS = [(xy[0], xy[1], s) for xy, s in zip(XY, S)]

        # 進行方向Rかつ最小のx座標
        # dict(y座標=そのy座標で最小のx座標)
        right_min = dict()
        # 進行方向Lかつ最大のx座標
        left_max = dict()

        for i in range(N):
            x, y, s = XYS[i]

            # 衝突判定
            if s == "R":
                # i番目の人の進行方向がRの時
                # 同じy座標に別の人がいる かつ i番目の人のx座標がその人よりも小さい時
                if y in left_max and x < left_max[y]:
                    # 衝突する
                    Yes()
            else:
                if y in right_min and right_min[y] < x:
                    Yes()

            # 進行方向Rの最小xと進行方向Lの最大xを更新
            if s == "R":
                # 同じy座標に別の人がいる時
                if y in right_min:
                    # 最小のX座標を選ぶ
                    right_min[y] = min(x, right_min[y])
                # 同じy座標に誰もいない場合
                else:
                    # 自分が最小のX座標
                    right_min[y] = x
            else:
                if y in left_max:
                    left_max[y] = max(x, left_max[y])
                else:
                    left_max[y] = x
        print("No")

if __name__ == "__main__":
    task = TaskC()
    task.run()
