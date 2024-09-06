
def maxProduct(nums: List[int]) -> int:
    res = float('-inf')
    currMin = currMax = 1
    for n in nums:
        currMin, currMax = min(currMax * n, currMin * n, n), max(currMax * n, currMin * n, n)
        if currMax > res: res = currMax
    return res

f = open('user.out', 'w')
for i in stdin:
    nums = list(map(int,i.rstrip()[1:-1].split(r',')))
    print(maxProduct(nums), file=f)
    
exit(0)       