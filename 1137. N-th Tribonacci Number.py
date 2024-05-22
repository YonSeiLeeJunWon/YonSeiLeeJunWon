Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def tribonacci(self, n: int) -> int:
        Fa=0
        Fb=1
        Fc=1
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        for i in range(3,n+1):
            Fn=Fa+Fb+Fc
            Fa=Fb
            Fb=Fc
            Fc=Fn
        return Fn
    
