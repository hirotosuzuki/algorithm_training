class TaskA:
    def run(self):
        a, b = map(int, input().split())
        c = a * b
        if c % 2 == 0:
            print("Even")
        else:
            print("Odd")

class TaskB:
    def run(self):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        pass

class TaskC:
    def run(self):
        pass

if __name__ == "__main__":
    task = TaskA()
    task.run()