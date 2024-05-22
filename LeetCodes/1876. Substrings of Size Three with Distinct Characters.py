Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countGoodSubstrings(self, s: str) -> int:
...         count=0
...         for i in range(len(s)-2):
...             goodString=s[i:i+3]
...             if goodString[0]!=goodString[1] and goodString[1]!=goodString[2] and goodString[0]!=goodString[2]:
...                 count+=1
...         return count
... 
