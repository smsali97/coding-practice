def findValidSubarray(nums, k):
  n = len(nums)
  dp = [1 for _ in range(n)]
  for i in range(1, n):
    if nums[i-1] + 1 == nums[i]:
      dp[i] = dp[i-1] + 1
  
  for end in range(n-1, -1, -1): 
    if dp[end] == k:
      if end - k >= 0 and dp[end - k] >= k:
        return nums[end-2*k+1:end+1]
    elif end > 0 and (dp[end] % k) == 0:
      return nums[end-2*k+1:end+1]
  return []

print(findValidSubarray([3, 2, 3, 4, 1, 2, 3, -1], 3))
print(findValidSubarray([2, 3, 4, 1, 2], 2))
print(findValidSubarray([3, 2, 3, 4, 5, 6, 7, -1], 3))
[2, 3, 4, 1, 2, 3]
[3, 4, 1, 2]
[2, 3, 4, 5, 6, 7]