class Task:
    def run(self):
        N, M = map(int, input().split())
        print(N + M)


if __name__ == "__main__":
    task = Task()
    task.run()
