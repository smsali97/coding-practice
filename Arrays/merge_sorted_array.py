class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1,nums2):
            arr = [0]*(len(nums1) + len(nums2))
            i, j = 0, 0
            for k in range(len(arr)):
                if i == len(nums1) or (j != len(nums2) and nums2[j] < nums1[i]):
                    arr[k] = nums2[j]
                    j += 1
                else:
                    arr[k] = nums1[i]
                    i += 1
            return arr
        arr = merge(nums1,nums2)
        n = len(arr)
        if n % 2 == 0:
            return ( arr[ n//2 ] + arr[n // 2 - 1]  )/2
        else:
            return arr[n//2]
            