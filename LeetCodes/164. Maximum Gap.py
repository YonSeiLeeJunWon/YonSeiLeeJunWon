Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maximumGap(self, nums: List[int]) -> int:
...         nums.sort()
...         max_gap=-1
...         if len(nums)==1:
...             return 0
...         for i in range(len(nums)-1):
...             if nums[i+1]-nums[i]>max_gap:
...                 max_gap=nums[i+1]-nums[i]
...         return max_gap
...         
