class TaskA:
    def run(self):
        V, A, B, C = map(int, input().split())
        pass

class TaskB:
    def run(self):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        pass

class TaskC:
    def run(self):
        N, M = map(int, input().split())
        K = []
        S = []
        for m in M:
            input = map(int, input().split())
            K.append(input[0])
            S.append(input[1:])
        P = map(int, input().split())



if __name__ == "__main__":
    task = TaskC()
    task.run()