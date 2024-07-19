class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        outer = 0
        maxed = 0
        context = {}

        while outer < len(s) + 1:
            inner = 0
            while inner < len(s) + 1:
                if s[outer: inner] == s[outer: inner][::-1]:
                    if len(s[outer: inner]) > maxed:
                        maxed = len(s[outer: inner])
                        context[maxed] = s[outer: inner]
                inner += 1
            outer += 1        
        return context[maxed]



print(Solution().longestPalindrome(s = "babad"))
print(Solution().longestPalindrome(s = "cbbd"))
print(Solution().longestPalindrome(s = "ac"))
print(Solution().longestPalindrome(s = "a"))
print(Solution().longestPalindrome(s = "abb"))
print(Solution().longestPalindrome(s = "ccd"))
print(Solution().longestPalindrome(s = "aacabdkacaa"))
# print(Solution().longestPalindrome(s = "txzokgefxajgkrlhllbqmcrtbjpppdzugzketdvlaxametkejdfbcwxijjjywjzoedqduensgouechpbdthevggtdelqyejxvybvmttbkheqfyiartxmmuxbkixgslcmjondweiyuvztqntkmvkxqqlfxgotaexzejnmfrhvkgaxyxdxasxrjevzwfvwvmxqikvsfbhhznjsvrlzkwionopahxhcetbsacwrazeciknyczsrxpbblvskzfaimaoyxfcwcsfxlulcezkbiszclkcfawqefwbhalyqjtvedlwigklrkuzyfamqjgjmytxytrlwhttelgttxlizpypwccfhwhwtzyawxyjqnynfdgrqixbwfahrjvvoowehmhyllnfhnnaswfmjitjbftpyvbfgtywcvhcziempcmxlgfuktengaakiwbovlfdtkropqvntuawouofuebfqojpmbodeaaedobmpjoqfbeufouowautnvqporktdflvobwikaagnetkufglxmcpmeizchvcwytgfbvyptfbjtijmfwsannhfnllyhmhewoovvjrhafwbxiqrgdfnynqjyxwayztwhwhfccwpypzilxttgletthwlrtyxtymjgjqmafyzukrlkgiwldevtjqylahbwfeqwafcklczsibkzeclulxfscwcfxyoamiafzksvlbbpxrszcynkicezarwcasbtechxhaponoiwkzlrvsjnzhhbfsvkiqxmvwvfwzvejrxsaxdxyxagkvhrfmnjezxeatogxflqqxkvmktnqtzvuyiewdnojmclsgxikbxummxtraiyfqehkbttmvbyvxjeyqledtggvehtdbphceuogsneudqdeozjwyjjjixwcbfdjektemaxalvdtekzguzdpppjbtrcmqbllhlrkgjaxfegkozxt"))