class Task:
    def run(self):
        A, B, C, X = map(int, input().split())
        # print(N + M)
        if X <= A:
            answer = 1
        elif X>A and X<=B:
            answer = C / (B - A)
        else:
            answer = 0
        print(answer)





if __name__ == "__main__":
    task = Task()
    task.run()
