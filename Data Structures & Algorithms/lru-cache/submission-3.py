class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right =  Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node: Node) -> None:
        # [prev] <-> [node] <-> [right]
        prev = self.right.prev
        prev.next, node.prev = node, prev
        self.right.prev, node.next = node, self.right

    def remove(self, node: Node) -> None:
        # [prev] <-> [node] <-> [next]
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
