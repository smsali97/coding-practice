class Solution:
    def partition(self, s: str) -> List[List[str]]:
        total_partitions = []
        def is_palindrome(substr):
            return substr == substr[::-1]

        def rec(index=0,partitions=[]):
            # base case
            if index == len(s):
                if partitions:
                    total_partitions.append(partitions)
                return
            for ending_index in range(index,len(s)):
                substr = s[index:ending_index+1]
                can_partition = is_palindrome(substr) # has to be inclusive
                if can_partition:
                    rec(ending_index+1,partitions + [substr])
        rec()
        return total_partitions


