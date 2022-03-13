class TaskA:
    def run(self):
        V, A, B, C = map(int, input().split())
        pass

class TaskB:
    def run(self):
        A = int(input())
        B = int(input())
        C = int(input())
        X = int(input())

        counter = 0
        for a in range(A+1):
            for b in range(B+1):
                for c in range(C+1):
                    total = 500 * a + 100 * b + 50 * c
                    if total == X:
                        counter += 1
        print(counter)

class TaskC:
    def run(self):
        pass

if __name__ == "__main__":
    task = TaskB()
    task.run()