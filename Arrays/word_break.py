class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for w in wordDict:
                start_idx = i - len(w)
                if start_idx < 0: continue # not possibe
                if dp[start_idx] and s[start_idx:i] == w:
                    dp[i] = dp[start_idx]
                    break
        return dp[-1]

                


        
        def wordLiesInString(s,w):
            if len(w) > len(s): return False # too big
            for i in range(len(w)):
                if w[i] != s[i]: return False
            return True
        # (cats)andog
        # exit: if we have an empty string, we have effectively reached the end
        # until we have a nonempty str
            # for word in worddict
                # if word lies in str (check first char)
                    # if yes then recur on remaining substring
        mem = {}
        def rec(s):
            if s in mem: return mem[s]
            if len(s) == 0:
                return True
            options = []
            for w in wordDict:
                if wordLiesInString(s,w):
                    start_idx = len(w)
                    options.append(rec(s[start_idx:]))
            ans = any(options)
            mem[s] = ans
            return ans
        return rec(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for w in wordDict:
                start_idx = i - len(w)
                if start_idx < 0: continue # not possibe
                if dp[start_idx] and s[start_idx:i] == w:
                    dp[i] = dp[start_idx]
                    break
        return dp[-1]

                


        
        def wordLiesInString(s,w):
            if len(w) > len(s): return False # too big
            for i in range(len(w)):
                if w[i] != s[i]: return False
            return True
        # (cats)andog
        # exit: if we have an empty string, we have effectively reached the end
        # until we have a nonempty str
            # for word in worddict
                # if word lies in str (check first char)
                    # if yes then recur on remaining substring
        mem = {}
        def rec(s):
            if s in mem: return mem[s]
            if len(s) == 0:
                return True
            options = []
            for w in wordDict:
                if wordLiesInString(s,w):
                    start_idx = len(w)
                    options.append(rec(s[start_idx:]))
            ans = any(options)
            mem[s] = ans
            return ans
        return rec(s)

