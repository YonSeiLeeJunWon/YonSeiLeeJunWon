Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maxProductDifference(self, nums: List[int]) -> int:
...         max_1=max(nums)
...         nums.remove(max_1)
...         max_2=max(nums)
...         min_1=min(nums)
...         nums.remove(min_1)
...         min_2=min(nums)
...         return max_1*max_2-(min_1*min_2)
