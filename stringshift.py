class Solution:
    def stringShift(self, s: str, shift: list) -> str:
        lst = [c for c in s]
        shift_amt = 0
        for direction, amt in shift:
            if direction is 1:
                shift_amt += amt
            else:
                shift_amt += -amt
        shift_amt = shift_amt % len(s)
        print(shift_amt)
        for _ in range(shift_amt):
            lst.insert(0,lst.pop())
        return ''.join(lst)
            