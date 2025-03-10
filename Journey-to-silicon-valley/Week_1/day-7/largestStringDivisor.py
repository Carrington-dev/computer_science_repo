# 1071. Greatest Common Divisor of Strings

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ''
        if str1 + str2 != str2 + str1:
            return divisor
        size = math.gcd(len(str1), len(str2))
        return str2[:size]


print(Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(Solution().gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(Solution().gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXX"))
# print(Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))