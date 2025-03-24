class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        opening = set("[({")
        closing = set("}])")
        ctx = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        count = 0
        for i in s:
            if i in opening:
                stack.append(i)
                count += 1
            elif i in closing:
                try:
                    if stack[-1] == ctx.get(i):
                        stack.pop()
                    else:
                        return False
                except:
                    return False
        return True if len(stack) == 0 else False
