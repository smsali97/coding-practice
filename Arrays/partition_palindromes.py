class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substr,start,end):
            l = start
            r = end
            while l <= r:
                if substr[l] != substr[r]: return False
                l += 1
                r -= 1
            return True
        all_partitions = []
        def rec(i=0,path=[]):
            if i == len(s):
                all_partitions.append(path[:])
            for j in range(i,len(s)):
                if is_palindrome(s,i,j):
                    path.append(s[i:j+1]) # j inclusive
                    rec(j+1,path) # recur on remaining
                    path.pop() # backtrack
        rec()
        return all_partitions