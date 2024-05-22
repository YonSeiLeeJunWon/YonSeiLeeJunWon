Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(0,n+1):
            total=0
            ppp=i
            while ppp>0:
                if ppp%2==1:
                    total+=1
                ppp=ppp//2 
            lst.append(total)
        return lst
    
