from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        negatives = { ")", "]", "}",}
        positives = { "(", "[", "{",}
        counter = 0

        opposite_brackets = dict()

        opposite_brackets[')'] = "("
        opposite_brackets['('] = ")"
        opposite_brackets['['] = "]"
        opposite_brackets[']'] = "["
        opposite_brackets['}'] = "{"
        opposite_brackets['{'] = "}"

        dynamic_brackets = set()
        for i in s:
            if i in negatives:
                if counter < 0:
                    return False
                else:
                    if i in dynamic_brackets:
                        dynamic_brackets.pop()
                        counter -= 1
                    else:
                        return False
            if i in positives:
                if counter < 0:
                    return False
                counter += 1
                dynamic_brackets.add(opposite_brackets[i])

        if counter != 0:
            return False
        return True
    

print(Solution().isValid("{[]}"))
print(Solution().isValid("([)]"))
print(Solution().isValid("[({])}"))