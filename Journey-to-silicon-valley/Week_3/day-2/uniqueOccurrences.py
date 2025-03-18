class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        context = {}
        for i in arr:
            if context.get(i) == None:
                context[i] = 1
            else:
                context[i] += 1
        count = { j:i for i, j in context.items()}
        return len(count) == len(context)
