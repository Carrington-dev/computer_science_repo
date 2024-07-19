class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        original = s
        s = self.clean_word(s)
        print("s = ", s)
        if len(s) == 0 or len(s) == 1:
            return len(s)
        maxed = 0
        outer = 0
        while outer < len(s):
            inner = 0
            while inner < len(s) + 1:
                try:
                    if s[outer] != s[inner]:
                        pass
                    else:
                        if len(s[outer: inner]) > maxed and s[outer: inner] in original:
                            maxed = len(s[outer: inner ])
                except:
                    pass
                inner += 1
            outer += 1
        return maxed

    def clean_word(self, s):
        if s == "" or len(s) == 1:
            return s
        new_s = [ i for i in s]
        for i in range(len(s) - 1):
            inner = 1
            try:
                while s[i] == s[inner + i]:
                    # print(s[i] == s[inner + i], s[i] , s[inner + i], )
                    new_s[inner + i] = "#"
                    inner += 1
            except:
                pass
        return "".join([i for i in new_s if i != "#"])
        
    def clean_wordTwo(self, s):
        if s == "" or len(s) == 1:
            return s
        s = [ i for i in s]
        previous = 0
        while previous < len(s) - 1 :
            try:
                counter = 0
                while s[previous] == s[previous + counter]:
                    s[previous+1] = ""
                    counter += 1
            except:
                pass
            previous += 1
        return "".join(s)
    


# print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))
# print(Solution().lengthOfLongestSubstring(s = "bbbb"))
# # print(Solution().clean_word(s = "bbbb"))
# print(Solution().lengthOfLongestSubstring(s = "babad"))
print(Solution().lengthOfLongestSubstring(s = "pwwkew"))
# print(Solution().lengthOfLongestSubstring(s = "cbbd"))
# print(Solution().lengthOfLongestSubstring(s = "ac"))
# print(Solution().lengthOfLongestSubstring(s = "a"))
# print(Solution().lengthOfLongestSubstring(s = "abb"))
# print(Solution().lengthOfLongestSubstring(s = "ccd"))
# print(Solution().lengthOfLongestSubstring(s = "aacabdkacaa"))
# print(Solution().lengthOfLongestSubstring(s = "txzokgefxajgkrlhllbqmcrtbjpppdzugzketdvlaxametkejdfbcwxijjjywjzoedqduensgouechpbdthevggtdelqyejxvybvmttbkheqfyiartxmmuxbkixgslcmjondweiyuvztqntkmvkxqqlfxgotaexzejnmfrhvkgaxyxdxasxrjevzwfvwvmxqikvsfbhhznjsvrlzkwionopahxhcetbsacwrazeciknyczsrxpbblvskzfaimaoyxfcwcsfxlulcezkbiszclkcfawqefwbhalyqjtvedlwigklrkuzyfamqjgjmytxytrlwhttelgttxlizpypwccfhwhwtzyawxyjqnynfdgrqixbwfahrjvvoowehmhyllnfhnnaswfmjitjbftpyvbfgtywcvhcziempcmxlgfuktengaakiwbovlfdtkropqvntuawouofuebfqojpmbodeaaedobmpjoqfbeufouowautnvqporktdflvobwikaagnetkufglxmcpmeizchvcwytgfbvyptfbjtijmfwsannhfnllyhmhewoovvjrhafwbxiqrgdfnynqjyxwayztwhwhfccwpypzilxttgletthwlrtyxtymjgjqmafyzukrlkgiwldevtjqylahbwfeqwafcklczsibkzeclulxfscwcfxyoamiafzksvlbbpxrszcynkicezarwcasbtechxhaponoiwkzlrvsjnzhhbfsvkiqxmvwvfwzvejrxsaxdxyxagkvhrfmnjezxeatogxflqqxkvmktnqtzvuyiewdnojmclsgxikbxummxtraiyfqehkbttmvbyvxjeyqledtggvehtdbphceuogsneudqdeozjwyjjjixwcbfdjektemaxalvdtekzguzdpppjbtrcmqbllhlrkgjaxfegkozxt"))


"""

pwkew
"""