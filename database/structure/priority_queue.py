import abc
import heapq

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
    """binary heapを使った優先度付きキュー
    挿入：O(logN)
    削除：O(logN)
    最小値取得：O(1)
    """
    def __init__(self, values: list[int]):
        self.heap = values
        heapq.heapify(self.heap)
    
    def insert(self, key: int, value: int) -> None:
        heapq.heappush(self.heap, value)
    
    def get_min(self) -> int | None:
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def delete_min(self) -> None:
        heapq.heappop(self.heap)

    def kth_smallest(self, k: int) -> int:
        return heapq.nsmallest(k, self.heap)[-1]

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        # kより要素数が多い場合は消す
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

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

    # https://docs.python.org/ja/3/library/queue.html
    # from queue import PriorityQueue

    # pq = PriorityQueue()
    # pq.put(1)
    # pq.get()