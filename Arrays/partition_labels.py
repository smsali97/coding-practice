class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # "ababcbacadefegdehijhklij"
        # substrina
        # groups of repeating chars as many as posisble
        # 'a'babacbac'a' because we got an a we have to clump them together
        # how do we know if theyre part of the same partition store their last index
        
        last_index = {}
        for i,c in enumerate(s):
            last_index[c] = i

        parts = []  
        start_at = 0
        ends_at = 0
        for i,c in enumerate(s):
            last_idx = last_index[c]
            if i <= ends_at:
                ends_at = max(last_idx,ends_at) # push ends at if you find a later index
            else:
                # you crossed the last index , time to start a new partition!
                parts.append(ends_at - start_at + 1)
                ends_at = last_idx
                start_at = i
        
        parts.append(ends_at - start_at + 1)
        return parts
        
                        


            

            


