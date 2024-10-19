class RandomizedSet:
    import random

    def __init__(self):
        self.arr = []
        self.val_to_idx = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx: return False
        self.arr.append(val)
        self.val_to_idx[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx: return False
        # swap out the last element and the current element
        idx = self.val_to_idx[val]
        
        last_element = self.arr[-1]

        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        # update its idx
        self.val_to_idx[last_element] = idx
        
        # note if element is already last element this wont do anything

        del self.val_to_idx[val]
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        # for a set of indices find out the 'random' id
        random_idx = random.randint(0,len(self.arr)-1)
        # indices have to be in a consecutive range
        return self.arr[random_idx] 

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()