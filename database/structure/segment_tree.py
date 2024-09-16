# https://www.slideshare.net/slideshow/ss-3578491/3578491
# https://qiita.com/june19312/items/e77485bfd9ba521ad060
import abc

class SegmentTreeADT(metaclass=abc.ABCMeta):
    """
    各ノードが区間に対応する完全二分木
    """

    @abc.abstractmethod
    def __init__(self, n: int) -> None:
        """
        n: 要素数
        self.size: 完全二分木の「葉」のノード数(2の冪乗): 2**(size-1) < n < 2**size
        self.data: 完全二分木のノード数の長さを持つリスト
        """
        self.size = 1
        while self.size < n:
            self.size *= 2

        self.data = [0] * (2 * self.size - 1)

    @abc.abstractmethod
    def update(self, position: int, value: int) -> None:
        """positionにvalueを代入する
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def query(self, left: int, right: int, a: int, b: int, position: int) -> None:
        raise NotImplementedError()

class SegmentTreeRMQ(SegmentTreeADT):
    """
    区間の最大値を求める(Range Maximum Query)
    """

    def __init__(self, n: int) -> None:
        super().__init__(n)

    def update(self, position: int, value: int) -> None:
        assert 0 <= position < self.size

        # 場所positionに対応する一番下(葉)のノードの位置を調べる
        # [N段目のノード数] = [1 ~ N-1段目のノード数の合計] + 1
        position += self.size - 1
        # 葉の値を更新
        self.data[position] = value
        # 葉から上に向かって更新
        while position > 0:
            # あるノードnの親ノードは(n-1)//2
            position = (position - 1) // 2
            # 親ノードの値は子ノードの最大値で更新
            # あるノードnの子ノードは2n+1, 2n+2
            self.data[position] = max(
                self.data[position * 2 + 1],
                self.data[position * 2 + 2],
            )
        print(f"data: {self.data}")

    def query(self, left: int, right: int, a: int, b: int, node_index: int) -> None:
        print(left, right, a, b, node_index)
        assert 0 <= left < right <= self.size
        assert 0 <= a <= b <= self.size
        assert 0 <= node_index < 2 * self.size - 1

        # 開区間[left, right)が開区間[a, b)を一切含まない場合
        if right <= a or b <= left:
            return float('-inf')
        
        # 開区間[left, right)が開区間[a, b)を完全に含む場合
        if left <= a and b <= right:
            return self.data[node_index]
        
        # 開区間[left, right)が開区間[a, b)に部分的に含まれる場合
        middle = (a + b) // 2
        # [a, middle)
        answer_left = self.query(left, right, a, middle, node_index * 2 + 1)
        # [middle, b)
        answer_right = self.query(left, right, middle, b, node_index * 2 + 2)
        return max(answer_left, answer_right)

class SegmentTreeRSQ(SegmentTreeADT):
    """
    区間の合計値を求める(Range Sum Query)
    """

    def __init__(self, n: int) -> None:
        super().__init__(n)

    def update(self, position: int, value: int) -> None:
        pass

    def query(self) -> None:
        pass

if __name__ == '__main__':
    """
    0(53)
    1(34) 2(53)
    3(29) 4(34) 5(13) 6(53)
    """
    rmq = SegmentTreeRMQ(4)
    rmq.update(0, 29)
    rmq.update(1, 34)
    rmq.update(2, 13)
    rmq.update(3, 53)
    res = rmq.query(0, 1, 0, rmq.size, 0)
    assert res == 29
