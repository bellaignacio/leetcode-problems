class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash = {} # { val: index }

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.list.append(val)
            self.hash[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            lastEl = self.list[-1]
            idx = self.hash[val]

            # swap target value w last value
            self.list[idx] = lastEl
            self.hash[lastEl] = idx

            # remove last value in O(1)
            self.list.pop()

            # update hash map
            del self.hash[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
