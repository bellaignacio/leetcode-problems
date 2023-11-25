class Node:

    def __init__(self, end = False):
        self.children = [None] * 26
        self.end = end


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            i = ord(char) - ord('a') # makes sure children[0] is a, children[1] is b, children[2] is c, ..., children[25] is z
            if current.children[i] == None:
                current.children[i] = Node()

            current = current.children[i] # create / traverse down path

        current.end = True # mark the last node as the end of a word

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            i = ord(char) - ord('a')
            if current.children[i] == None:
                return False
            else:
                current = current.children[i]

        return True if current.end else False

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            i = ord(char) - ord('a')
            if current.children[i] == None:
                return False
            else:
                current = current.children[i]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
