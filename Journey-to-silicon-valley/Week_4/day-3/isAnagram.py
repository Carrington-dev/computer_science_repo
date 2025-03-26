class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        old_context = {}
        new_context = {}

        if len(s) != len(t):
            return False

        for i in s:
            if old_context.get(i) != None:
                old_context[i]  += 1
            else:
                old_context[i]  = 1

        for i in t:
            if new_context.get(i) != None:
                new_context[i]  += 1
            else:
                new_context[i]  = 1

        for k, v in new_context.items():
            if old_context.get(k) != v:
                return False
        
        return True
