# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

#     Each student gets one packet.
#     The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

# Examples:

#     Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
#     Output: Minimum Difference is 2 


# Sort it!
# 2 3 4 7 9 12 56
#  1 1 3  2 3 44
#  

def min_difference_chocolates(nums, m):
    import sys
    min_diff = sys.maxsize

    nums.sort()

    for i in range(len(nums) - m + 1):  
        min_diff = min(min_diff,nums[i + m  - 1] - nums[i])
    
    return min_diff


print(min_difference_chocolates([3, 4, 1, 9, 56, 7, 9, 12],5))