from collections import defaultdict

class Solution:
    def countElements(self, arr: list) -> int:
        mydict = defaultdict(int)
        
        for num in arr:
            mydict[num] = mydict[num] + 1
        
        ctr = 0
        for key in mydict.keys():
            if key+1 in mydict.keys():
                ctr += mydict[key]
        return ctr
        