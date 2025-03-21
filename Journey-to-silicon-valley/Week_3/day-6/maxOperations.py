class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        context  = {}
        for i in range(len(nums)):
            if nums[i] in context:
                context[nums[i]] += 1
            else:
                context[nums[i]] = 1

        def isValid(context, k):
            for key, val in context.items():
                if k - key != key:
                    if context.get(k - key) and context.get(k - key) > 0:
                        return True
                else:
                    if context.get(k - key) >= 2:
                        return True
            return False

        c = 0
        while isValid(context, k):
            for ky, v in context.items():
                
                if context.get(ky) and context.get(k - ky):
                    if ky != k -ky:
                        context[ky] -= 1 
                        context[k - ky] -= 1 
                    else:
                        context[ky] -= 2 

                    c += 1

        # return [key for key, v in context.items() if v > 0]
        # print(sum([v for key, v in context.items() if v > 0]))
        print(context)
        return c
