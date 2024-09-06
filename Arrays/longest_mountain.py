class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        def is_peak(arr: List[int], i: int):
            return i >= 1 and i <= len(arr) - 2 and arr[i-1] < arr[i] and arr[i] > arr[i+1]
        max_len = 0
        for i, val in enumerate(arr[1:]):
            found_peak = is_peak(arr,i)
            if found_peak:
                L = i
                R = i
                curr_len = 1
                while L > 0:
                    if arr[L] > arr[L-1]:
                        L -= 1
                        curr_len += 1
                    else:
                        break
                while R < len(arr) - 1:
                    if arr[R] > arr[R+1]:
                        R += 1
                        curr_len += 1
                    else:
                        break
                max_len = max(curr_len,max_len)
        return max_len