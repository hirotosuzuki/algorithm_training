# 連結リスト

class LinkedListNode:
    def __init__(self, data: any):
        self.data = data
        self.next: LinkedListNode = None

class LinkedList:
    def __init__(self, head: LinkedListNode | None) -> None:
        self.head = head

    def insert_node(self, node: LinkedListNode, position: int) -> None:
        pass

    def delete_node(self, position: int) -> None:
        pass

    def delete(self) -> None:
        pass

    # 循環しているかどうかを判定する
    def has_cycle(self) -> bool:
        visited_nodes = set()
        current_node = self.head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False

    # 循環の開始地点を検出する
    # setを使う方法
    def detect_cycle_hashmap(self) -> LinkedListNode | None:
        visited = set()
        current = self.head
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        return None

    # 循環の開始地点を検出する
    # フロイドの循環検出アルゴリズム
    def detect_cycle_floyd(self) -> LinkedListNode | None:
        # fastポインタ
        fast = self.head
        # slowポインタ
        slow = self.head

        while fast and fast.next:
            # slowは1ステップずつ進む
            slow = slow.next
            # fastは2ステップずつ進む
            fast = fast.next.next

            # fastとslowがkステップで出会う
            # fastとslowの進んだ距離の差は2k - k = k
            # kの差があるのに同じ場所にいるということは、kがループ長の整数倍であることを示している
            # fastとslowは共にループの整数倍の距離を進んだ位置にいる
            # fastかslowのどちらかに開始地点からループ開始までの距離を足してあげると
            # (ループ開始までの距離 + ループ長の整数倍)の座標 = (ループ開始までの距離)の座標 => ループが開始した地点にいることになる！
            if slow == fast:
                # slowを先頭に戻す(fastを戻すのでも良い)
                # ループ開始までの距離をslowに測ってもらう
                slow = self.head
                while slow != fast:
                    # fastもslowも1ずつ進ませる
                    slow = slow.next
                    fast = fast.next
                # fastとslowがもう一度出会った時、そこがサイクルの開始点
                return slow

    # 値が重複するノードを削除する. 連結リストはソートされている前提.
    # [1, 2, 2, 3, 4] -> [1, 2, 3, 4]
    def delete_duplicates_from_sorted_list(self) -> None:
        if self.head is None:
            return self.head

        previous = self.head
        current = self.head.next

        while current:
            if current.data == previous.data:
                previous.next = current.next
            else:
                previous = current
            current = current.next

    # 重複しているノードを残さずに削除する. [1, 2, 2, 3, 4] -> [1, 3, 4]
    def delete_all_duplicates_from_sorted_list(self) -> None:
        if self.head is None:
            return self.head

        fake = LinkedListNode(-1)
        fake.next = self.head

        prev = fake
        current = self.head

        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = prev.next
