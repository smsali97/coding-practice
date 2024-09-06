class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False

        mem = {}  # Memoization dictionary

        def rec(i=0, j=0, k=0):
            if (i, j, k) in mem: 
                return mem[(i, j, k)]  # Return memoized result if available

            # Base cases:
            if k == n3:  # Reached the end of s3
                return i == n1 and j == n2  # Check if we've also reached the end of s1 and s2

            result = False  # Initialize result to False

            if i < n1 and s1[i] == s3[k]:
                result |= rec(i + 1, j, k + 1)  # Explore taking a character from s1

            if j < n2 and s2[j] == s3[k]:
                result |= rec(i, j + 1, k + 1)  # Explore taking a character from s2

            mem[(i, j, k)] = result  # Memoize the result
            return result

        return rec()  # Start the recursive process