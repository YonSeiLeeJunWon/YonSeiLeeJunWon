Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        Rcount=0
        Lcount=0
        for i in s:
            if i =="R":
                Rcount+=1
            else:
                Lcount+=1
            if Rcount==Lcount:
                count+=1
                Rcount=0
                Lcount=0
        return count
    
