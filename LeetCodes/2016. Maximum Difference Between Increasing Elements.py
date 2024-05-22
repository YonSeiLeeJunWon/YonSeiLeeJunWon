Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maximumDifference(self, nums: List[int]) -> int:
...         max_value=-1
...         for i in range(len(nums)):
...             for j in range(len(nums)):
...                 if i<j and nums[i]<nums[j] and nums[j]-nums[i]>max_value:
...                     max_value=nums[j]-nums[i]
...         return max_value
