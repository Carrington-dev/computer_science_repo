class Solution:
    def isHappy(self, n: int) -> bool:
        summed =  sum([int(number) * int(number) for number in str(n)])
        summed_sets = set()
        while summed > 2:
            summed =  sum([int(number) * int(number) for number in "0"+ str(summed)])
            if summed not in summed_sets:
                summed_sets.add(summed)
            else:
                return False
        return True if summed == 1 else False
        
print(Solution().isHappy(19))
print(Solution().isHappy(2))
print(Solution().isHappy(24))
print(Solution().isHappy(9))