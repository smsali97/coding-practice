# Given a binary array data, 
# return the minimum number of swaps 
# required to group all 1’s present in the array 
# together in any place in the array.


def min_swaps_required_for_all_1s(nums):

    # windows size is the number of 1s    
    window_size = sum(nums)

    # set to max value
    min_swaps = float('inf') 
    # current ones in window
    ones_in_window = 0

    for i in range(len(nums)):
        # found a 1
        ones_in_window += nums[i]
        # if window size is reached
        if i >= window_size:
            ones_in_window -= nums[i - window_size]
        # if we have enough 1s in the
        if i >= window_size - 1:
            # take the global minimum
            min_swaps = min(min_swaps,window_size - ones_in_window)
    return min_swaps


    
    

A = [1,0,1,0,1]
A = [0,0,0,1,0] # passing
A = [1,0,1,0,1,0,0,1,1,0,1]

A = [0,0,0,0,0]
A = [1,1,1,1,1]
print(min_swaps_required_for_all_1s(A))

