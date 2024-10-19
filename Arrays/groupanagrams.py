from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        
        anagram_dict = defaultdict(set)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].add(word)
            anagram_dict[sorted_word] = [word]
        
        return anagram_dict.values()
        