import bisect

def binary_search_1(data: list[int], value: int) -> int:
    return bisect.bisect_left(data, value)


def binary_search_2(data: list[int], value: int) -> int:
    """二分探索
    Args:
        data (List[int]): 昇順にソートされたリスト
        value (int): 探索する値
    Returns:
        int: 見つかった場合はそのインデックス、見つからない場合は挿入するインデックス
    """
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2

        if data[mid] == value:
            return mid
        # data[left] < data[mid] < value < data[right]
        elif data[mid] < value:
            left = mid + 1
        # data[left] <  value < data[mid] < data[right]
        else:
            right = mid

    return left
