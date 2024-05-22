Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def heightChecker(self, heights: List[int]) -> int:
...         count=0
...         lst=heights.copy()
...         heights.sort()
...         for i in range(len(heights)):
...             if heights[i]!=lst[i]:
...                 count+=1
...         return count
