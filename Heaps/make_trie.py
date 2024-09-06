class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not c in node:
                node[c] = {}
            node = node[c]
        node['*'] = True

    def search(self, woard: str) -> bool:
        node = self.root
        for c in word:
            if not c in node: return False
            node = node[c]
        return '*' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not c in node: return False
            node = node[c]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)