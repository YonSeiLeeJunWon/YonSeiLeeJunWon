Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num>0:
            if num%2==0:
                num=num/2
                count+=1
            else:
                num=num-1
                count+=1
        return count
    
