Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def addDigits(self, num: int) -> int:
        result=0
        if num==0:
            return 0
        
        while result>=10 or result==0:
            result=0
            for digit in str(num):
                result=result+int(digit)
            num=result

        return result
    
