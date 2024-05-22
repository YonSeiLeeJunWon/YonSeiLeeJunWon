Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def differenceOfSums(self, n: int, m: int) -> int:
...         sumnotdiv=0
...         sumdiv=0
...         for i in range(1,n+1):
...             if i%m==0:
...                 sumdiv=sumdiv+i
...             else:
...                 sumnotdiv=sumnotdiv +i
...         return sumnotdiv-sumdiv
