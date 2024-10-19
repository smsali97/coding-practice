class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # keep track of temperatures if you encouter
        # a higher temp check your and current if it matches and insert them accordingly
        answers = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # encountered a colder temp
            if not stack or stack[-1][0] > temp:
                stack.append((temp,i))
                continue

            # until you keep on finding a warmer temp
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                answers[idx] = (i-idx)
            stack.append((temp,i))
        return answers
        