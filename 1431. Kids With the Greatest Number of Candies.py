Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
...         maxValue=max(candies)
...         lst=[]
...         for i in candies:
...             if i+extraCandies>=maxValue:
...                 lst.append(True)
...             else:
...                 lst.append(False)
...         return lst
