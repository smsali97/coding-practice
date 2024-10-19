class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added_digits = list(digits)
        added_digits[-1] += 1
        carry = False
        for i in reversed(range(len(added_digits))):
            if carry:
                added_digits[i] += 1
                carry = False
            if added_digits[i] == 10:
                added_digits[i] = 0
                carry = True
            else:
                break
        if carry: added_digits.insert(0,1)
        return added_digits