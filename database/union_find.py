# 素集合データ構造

class UnionFindTree:
    def __init__(self, n: int) -> None:
        # ノードの数
        self.n = n
        # 各ノードのrootノードの番号
        self.parents = [-1] * n
        # 各ノードの属する木の高さ
        self.ranks = [0] * n

    # 要素xが属する集合のrootを返す
    def find(self, x: int) -> int:
        # xが根の場合はxを返す
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮
            # [再帰的に根を探す過程]で通ったノードの親を根に書き換える
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属する集合と要素yが属する集合を併合する
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        # すでに同じ集合に属していた場合は何もしない
        if root_x == root_y:
            return False

        # rankが小さい方をrankが大きい方にくっつける
        if self.ranks[root_x] < self.ranks[root_y]:
            # xのrootをyのrootにする
            self.parents[root_x] = root_y
        elif self.ranks[root_x] > self.ranks[root_y]:
            # yのrootをxのrootにする
            self.parents[root_y] = root_x
        else:
            # rankが同じ場合はどちらをrootにしてもよいが、xをrootにしてyをくっつける
            self.parents[root_y] = root_x
            # xにくっつけたのでx側のrankを1増やす
            self.ranks[root_x] += 1

        return True

    # 要素xと要素yが同じ集合に属しているかを返す
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def __str__(self) -> str:
        return f'parents: {self.parents}, ranks: {self.ranks}'
