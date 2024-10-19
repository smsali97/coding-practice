class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        class Trie:
            def __init__(self):
                self.root = {}
            
            def build(self, dictionary):
                for word in dictionary:
                    node = self.root
                    for c in word:
                        if c not in node: node[c] = {}
                        node = node[c]
                    node['*'] = {}
            
            def word_ends_at(self, word):
                node = self.root
                i = 0
                indexes = []
                for c in word:
                    if c not in node: return indexes
                    node = node[c]
                    i += 1
                    if '*' in node: indexes.append(i)
                return indexes
        
        trie = Trie()
        trie.build(dictionary)

        # 'leet'


        mem = {}
        def rec(i=0):
            if i == len(s): return 0
            if s[i:] in mem: return mem[s[i:]]

            opt1, opt2 = float('inf'), float('inf')

            opt1 = 1 + rec(i+1)        
            index_matches = trie.word_ends_at(s[i:])
            if index_matches: opt2 = min(rec(i+idx) for idx in index_matches)
            ans = min(opt1,opt2)
            mem[s[i:]] = ans
            return ans
        
        return rec()


            
