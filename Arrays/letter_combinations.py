class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        m = {
             2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
             7: "pqrs", 8: "tuv", 9: "wxyz"
             }
        options = []
        def rec(i=0,arr=[]):
            if i == len(digits):
                options.append(''.join(arr))
                return
            letters = list(m[int(digits[i])])
            for letter in letters:
                rec(i+1,arr + [letter])
        rec()
        return options
