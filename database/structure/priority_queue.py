import abc

"""binary heapを使った優先度付きキュー
挿入：O(logN)
削除：O(logN)
最小値取得：O(1)
"""


class PriorityQueueADT(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, key: int, value: int) -> None:
        """挿入
        Args:
            key (int): 挿入するキー
            value (int): 挿入する値
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_min(self) -> int | None:
        """最小値取得
        Returns:
            int: 最小値
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_min(self) -> None:
        """最小値削除
        """
        raise NotImplementedError()

class PriorityQueueUsingBinaryHeap(PriorityQueueADT):
    pass


if __name__ == "__main__":
    pq = PriorityQueueUsingBinaryHeap()
    pq.insert(1, 10)
    pq.insert(2, 20)
    pq.insert(3, 30)
    print(pq.get_min())  # 10
    pq.delete_min()
    print(pq.get_min())  # 20
    pq.delete_min()
    print(pq.get_min())  # 30
    pq.delete_min()
    print(pq.get_min())  # None