Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>1:
            if n%3!=0:
                return False
            else:
                n=n/3
        if n<=0:
            return False
        else:
            return True
        
    
