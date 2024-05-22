Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        Lst=[]
        for i in range(1,n+1):
            if n%i==0:
                Lst.append(i)
        if len(Lst)<k:
            return -1
        else:
            return Lst[k-1]
        
