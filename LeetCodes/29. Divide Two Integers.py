Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend*divisor==0:
            return 0
        elif dividend*divisor>0:
            if dividend*divisor==2147483648:
                return 2147483647
            else:
                return int(dividend/divisor)
        else:
            return int(dividend/divisor)
        
