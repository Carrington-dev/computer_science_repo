class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s):
            # print(t[i])
            new  = t.replace(t[i], s[i])
            print(new, s)
            if new == s:
                return True
            i += 1
        return False
print(Solution().isIsomorphic(s = "egg", t = "add"))
print(Solution().isIsomorphic(s = "foo", t = "bar"))
print(Solution().isIsomorphic(s = "paper", t = "title"))