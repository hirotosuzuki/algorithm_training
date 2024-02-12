#!/usr/bin/env python3
import math

def main():
    N = int(input())

    cost = 0
    black_boards = [N]
    while len(black_boards) > 0 and max(black_boards) >= 2:
        # 黒板から2以上の整数xを選ぶ
        for num in black_boards:
            if num >= 2:
                x = num
                black_boards.remove(num)
                cost += x
                lower = int(x/2)
                upper = math.ceil(x/2)
                if (lower > 1):
                    black_boards.append(lower)
                if (upper > 1):
                    black_boards.append(upper)
                break

    print(cost)

if __name__ == '__main__':
    main()