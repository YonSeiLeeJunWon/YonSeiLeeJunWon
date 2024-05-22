Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maximumCount(self, nums: List[int]) -> int:
...         pos_count=0
...         neg_count=0
...         for i in nums:
...             if i>0:
...                 pos_count+=1
...             elif i<0:
...                 neg_count+=1
...         return max(pos_count,neg_count)
