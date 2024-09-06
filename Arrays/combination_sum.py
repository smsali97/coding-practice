class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        def rec(i=0,comb=[],target=target):
            if target == 0: combs.append(comb)
            if i == len(candidates) or target <= 0: return
            candidate = candidates[i]
            rec(i,comb + [candidate], target-candidate) # allow for duplicates and pick it as well!
            rec(i+1,comb,target) # never include that i again
        rec()
        return combs