class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        context =  {}
        for i in nums:
            if context.get(i) != None:
                context[i] += 1
            else:
                context[i] = 1
        
        derived = [f for f, v in context.items() if v == 1]
        return derived[0]
