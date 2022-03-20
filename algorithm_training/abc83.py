class TaskA:
    def run(self):
        V, A, B, C = map(int, input().split())
        pass

class TaskB:
    def run(self):
        N, A, B = map(int, input().split())
        counter = 0
        for n in range(1, N+1):
            n_list = list(map(int, str(n)))
            sum_n = sum(n_list)
            if A <= sum_n and sum_n <= B:
                counter += n
        print(counter)

class TaskC:
    def run(self):
        pass

if __name__ == "__main__":
    task = TaskB()
    task.run()