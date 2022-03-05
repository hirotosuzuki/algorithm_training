class Task:
    def run(self):
        # N, M = map(int, input().split())
        # print(N + M)
        s = input()
        print("".join(sorted(s)))


if __name__ == "__main__":
    task = Task()
    task.run()
