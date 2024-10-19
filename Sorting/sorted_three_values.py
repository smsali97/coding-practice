from sortedcontainers import SortedList

sl = SortedList()
def find_and_remove(v, D):
    sl.add(v)

    idx = sl.index(v)
    if len(sl) < 3:
        return
    
    left, right = max(0, idx - 1),  min(len(sl) - 1, idx + 1)

    if left == idx or right == idx:
        # left, curr and right need to be distinct
        return
    
    if (abs(sl[left] - v) <= D and 
        abs(sl[right] - v) <= D and 
        abs(sl[right] - sl[left]) <= D):
        # print(sl, sl[left], v, sl[right], left, idx, right)
        vl = sl[left]
        vr = sl[right]
        sl.remove(vl)
        sl.remove(v)
        sl.remove(vr)

values = [1,10,7,-2,8]
D = 5   

for v in values:
    find_and_remove(v, D)

print(sl)