class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class Trie:
            def __init__(self):
                self.root = {}
                # * denotes ending
            def build_tree(self,words):
                for word in words:
                    node = self.root
                    for c in word:
                        if c not in node:
                            node[c] = {}
                        node = node[c]
                        # prefix_words
                        node['*'] = node.get('*',[]) + [word]

                                        
        prefix_trie = Trie()
        prefix_trie.build_tree(products)
        list_of_words = [[] for _ in searchWord]
        print(list_of_words)
        from heapq import heappop, heapify
        node = prefix_trie.root
        for i,char_to_search in enumerate(searchWord):
            if char_to_search in node:
                node = node[char_to_search]
                possible_words = node['*']
                min_length = min(3,len(possible_words))
                heapify(possible_words)
                top_3_sorted_words = [ heappop(possible_words) for _ in range(min_length) ]
                list_of_words[i] = top_3_sorted_words
            else:
                break
        return list_of_words
        

