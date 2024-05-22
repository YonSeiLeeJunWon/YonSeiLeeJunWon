Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def majorityElement(self, nums: List[int]) -> int:
...         count=0
...         candidate=None
...         
...         for num in nums:
...             if count==0:
...                 candidate=num
...             count+=1 if num==candidate else -1
...         
...         return candidate
