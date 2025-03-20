# Not Efficient
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def countVowels(sub_s):
            count = 0
            for i in sub_s:
                if i.lower() in {"a", "e","i","o", 'u'}:
                    count += 1
            return count
        
        maximum = 0
        for i in range(k, len(s)+1):
            if maximum < countVowels(s[i-k: i]):
                maximum = countVowels(s[i-k: i])
            print((s[i-k: k]))
        return maximum


        
