class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # A is predesc of B IFF one insertion max allowed in A == B
            # one insertion; mismatch of one character
        
        # A' predesc A predesc B [ wordchain length = 3]
          # ab        abc   abac          
          # length incareases by one

        # set of all words

        # for all word in chains:
        # if youve seen a word return the max_chain you can get from it
        # start from the end of a chain
            # for each c in word check if word excl. c exists if yes its a word chain
                    # 1 + subword

        length_of_word_chain = {}
        word_set = set(words)
        mem = {}
        def rec(word):
            if len(word) == 0: return 0
            if word in mem: return mem[word]
            max_length = 1
            for i,ch in enumerate(word):
                word_excl_ch = word[:i] + word[i+1:]
                if word_excl_ch in word_set:
                    max_length = max(max_length, 1 + rec(word_excl_ch))    
            mem[word] = max_length        
            return max_length

        max_len = 1
        for w in word_set:
            max_len = max(max_len,rec(w))
        return max_len
