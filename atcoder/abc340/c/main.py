#!/usr/bin/env python3
from functools import cache

# メモ化再帰
@cache
def get_cost(N: int) -> int:
    if N == 1:
        return 0
    else:
        # floor演算
        return get_cost(N//2) + get_cost((N+1)//2) + N

def main():
    N = int(input())
    cost = get_cost(N)
    print(cost)

if __name__ == '__main__':
    main()