from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        
        stack = deque()
        context = {}
        context['{'] = '}'
        context['('] = ')'
        context['['] = ']'
    

        counter = 0
        open  = 0
        close  = 0
        while counter < len(s):
            item = s[counter]
            if item in context:
                stack.append(item)
                open += 1
            else:
                close += 1
                try:
                    if item == context[stack.pop()]:
                        pass
                    else:
                        return False
                except:
                    return False
            counter += 1
        return True if close == open else False


"""
[][{}]{}
[][{}]{]}
"""
print(Solution().isValid("[][{]}()"))
print(Solution().isValid("[]{}()"))
print(Solution().isValid("[)"))
print(Solution().isValid("["))
print(Solution().isValid("[["))
print(Solution().isValid("(("))
print(Solution().isValid("[)]"))