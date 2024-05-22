Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def isUgly(self, n: int) -> bool:
        while n>1:
            if n%2==0:
                n=n/2
            elif n%3==0:
                n=n/3
            elif n%5==0:
                n=n/5
            else:
                return False
        if n==1:
            return True
        
