class Solution:
    def removeStars(self, s: str) -> str:
        collect = list()
        for i in range(len(s)):
            if s[i] == "*":
                collect.pop()
            else:
                collect.append(s[i])
        
        return "".join(collect)


print(Solution().removeStars(s = "leet**cod*e"))
print(Solution().removeStars(s = "erase*****"))

