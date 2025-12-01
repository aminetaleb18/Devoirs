class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                pal = s[i:j+1]
                if pal == pal[::-1]:
                    if len(pal) > len(res):
                        res = pal
        return res
mot=input("Saisir un mot :")
var=Solution().longestPalindrome(mot)
print(var)