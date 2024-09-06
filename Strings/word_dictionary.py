class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:  # Use 'not in' for better readability
                node[c] = {}
            node = node[c]
        node['*'] = {}  # Mark the end of a word

    def search(self, word: str) -> bool:
        def rec_search(i=0, node=self.root):
            if not node: 
                return False
            if i == len(word):
                return '*' in node  # Check for word ending only when 'i' reaches the end

            c = word[i]
            if c != '.':
                return c in node and rec_search(i + 1, node[c])  # Continue search if char matches
            else:
                # Search all possible branches for '.'
                return any(rec_search(i + 1, child) for child in node.values()) 

        return rec_search()