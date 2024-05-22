Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findMaxK(self, nums: List[int]) -> int:
...         while True:
...             a=max(nums)
...             if -a in nums:
...                 return a
...             else:
...                 nums.remove(a)
...             if nums==[]:
...                 return -1
