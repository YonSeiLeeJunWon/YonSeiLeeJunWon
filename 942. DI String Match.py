Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n=len(s)
        result=[]
        low, high = 0, n
        for i in s:
            if i=="I":
                result.append(low)
                low +=1
            else:
                result.append(high)
                high -=1
        result.append(low)
        return result
    
