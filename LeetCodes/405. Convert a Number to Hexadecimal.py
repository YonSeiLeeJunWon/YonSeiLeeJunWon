Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def toHex(self, num: int) -> str:
...         if num==0:
...             return "0"
...         
...         chars = "0123456789abcdef"
...         result = ""
...         if num<0:
...             num+=2**32
...         
...         while num>0:
...             digit=num%16
...             result=chars[digit]+result
...             num//=16
...         
...         return result
