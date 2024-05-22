Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def mySqrt(self, x: int) -> int:
        for j in range (0,x+1):
            if pow(j,2)<=x:
                if pow(j+1,2)>x:
                    return j
                    break
                else:
                    j=j+1
                    
