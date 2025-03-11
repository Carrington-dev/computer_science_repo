from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        context = {}
        
        for i in chars:
            if context.get(i) == None:
                context[i] = 1
            else:
                context[i] += 1
        
        final_list = []
        for letter, count in context.items():
            if count > 1 and count < 10:
                final_list.append(letter)
                final_list.append(str(count))
            elif count >= 10:
                final_list.append(letter)
                for i in str(count):
                    final_list.append(i)
            else:
                final_list.append(letter)

        
        return len(final_list)
    
print(Solution().compress(chars = ["a","a","b","b","c","c","c"]))
print(Solution().compress(chars = ["a",]))
print(Solution().compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))