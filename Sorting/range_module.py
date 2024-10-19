def b_left(arr, val):
    l = 0
    r = len(arr)

    while l < r:
        mid = (l + r) // 2

        if arr[mid][0] < val:
            l = mid + 1
        else:
            r = mid
    return l

class RangeModule:

    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        arr = self.arr
        left_index = b_left(arr, left)
        new_arr = []

        index = 0
        for i in range(len(arr) + 1):
            if i == left_index:
                new_arr.append([left, right])
            else:
                new_arr.append(arr[index])
                index += 1

        prev = new_arr[0]
        merged_arr = []
        i = 1

        while i < len(new_arr):
            cur = new_arr[i]

            if cur[0] <= prev[1]:
                prev = [min(prev[0], cur[0]), max(prev[1], cur[1])]
            else:
                merged_arr.append(prev)
                prev = cur
            i += 1
        
        merged_arr.append(prev)
        self.arr = merged_arr

    def queryRange(self, left: int, right: int) -> bool:
        arr = self.arr
        left_index = b_left(arr, left)
        
        if left_index < len(arr):
            if arr[left_index][0] == left:
                return arr[left_index][1] >= right

        if left_index - 1 >= 0:
            return (
                arr[left_index - 1][0] <= left and
                arr[left_index - 1][1] >= right
            )

        return False

    def removeRange(self, left: int, right: int) -> None:
        arr = self.arr
        new_arr = []

        if not arr:
            return

        for i in range(len(arr)):
            cur = arr[i]

            if right < cur[0] or left >= cur[1]:
                new_arr.append(cur)

            elif left <= cur[0] and right >= cur[1]:
                continue

            elif left <= cur[0] and right < cur[1]:
                new_arr.append([right, cur[1]])
            
            elif left > cur[0] and right >= cur[1]:
                new_arr.append([cur[0], left])

            elif left > cur[0] and right < cur[1]:                
                new_arr.append([cur[0], left])
                new_arr.append([right, cur[1]])

        self.arr = new_arr

            

            




# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)