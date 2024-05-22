Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multi=1
        Sum=0
        for i in str(n):
            multi=multi*int(i)
            Sum=Sum+int(i)
        return multi-Sum
    
