class Node:

    def __init__(self, end = False):
        self.children = {}
        self.end = end


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]

        current.end = True # mark the last node as the end of a word

    def search(self, word: str) -> bool:
        def _dfs(index, root):
            current = root

            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children.values():
                        if _dfs(i + 1, child):
                            return True
                    return False
                elif char not in current.children:
                    return False
                else:
                    current = current.children[char]

            return current.end

        return _dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
