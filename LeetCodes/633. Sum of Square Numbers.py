Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0,int(c**0.5)+1):
            if int((c-i**2)**0.5)==(c-i**2)**0.5:
                return True
        return False
    
