class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.length -= 1

    def push(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        self.length += 1
        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.DLL = DoublyLinkedList()
        self.hash = {}

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            self.DLL.remove(self.hash[key])
            self.hash[key] = self.DLL.push(self.hash[key])
            return self.hash[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.DLL.remove(self.hash[key])

        newNode = ListNode(key, value)
        self.hash[key] = self.DLL.push(newNode)

        if self.DLL.length > self.capacity:
            lru = self.DLL.head.next
            del self.hash[lru.key]
            self.DLL.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
