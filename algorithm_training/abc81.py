class TaskA:
    def run(self):
        S = input()
        counter = 0
        for s in S:
            if s == "1":
                counter += 1
        print(counter)

class TaskB:
    def run(self):
        N = int(input())
        A = list(map(int, input().split()))
        def is_even(A):
            for a in A:
                if a % 2 == 1:
                    return False
            return True
        counter = 0
        while is_even(A):
            A = [a/2 for a in A]
            counter += 1
        print(counter)


class TaskC:
    def run(self):
        pass

if __name__ == "__main__":
    task = TaskA()
    task.run()