Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix=strs[0]
        for word in strs[1:]:
            while word[:len(prefix)]!=prefix:
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

      
