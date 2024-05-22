Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def climbStairs(self, n: int) -> int:
        Fn=0
        Fa=2
        Fb=3
        for i in range(4,n+1):
            Fn=Fa+Fb
            Fa=Fb
            Fb=Fn
        if n==1:
            return 1
        elif n==2:
            return Fa
        elif n==3:
            return Fb
        else:
            return Fn
        
