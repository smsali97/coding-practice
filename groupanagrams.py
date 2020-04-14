from collections import Counter
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        
        anagram_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict.keys():
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        return anagram_dict.values()
        