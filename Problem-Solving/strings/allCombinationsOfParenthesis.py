from collections import deque
from itertools import product
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = ([["(", ")"]] * n * 2)
        all_strings = ["".join(i) for i in (list(product(*a)))]
        return set([ word for word in all_strings if self.isValid(word)])

    def isValid(self, string):
        if len(string) == 0:
            return True
        if len(string) == 1:
            return False
        opposites = {}
        opposites[")"] = "("
        opposites["("] = ")"
        positives = { "("}
        negatives = { ")" }
        stack = deque()
        stack.append(string[0])
        count = 0
        balance  = 0
        top = None
        while count < len(string):
            if balance < 0:
                return False
            if len(stack) > 0:
                top = stack.pop()
            
            if string[count] in positives:
                balance += 1
            elif string[count] in negatives:
                if opposites[string[count]] != top:
                    return False
                balance -= 1
            count += 1
        return True if balance == 0 else False
            

print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(3))
#print(Solution().isValid("()"))
#print(Solution().isValid(")(()))"))