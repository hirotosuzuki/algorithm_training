def binary_search(data, value) -> int:
    """二分探索
    Args:
        data (List[int]): 昇順にソートされたリスト
        value (int): 探索する値
    Returns:
        int: 見つかった場合はそのインデックス、見つからない場合は-1
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1