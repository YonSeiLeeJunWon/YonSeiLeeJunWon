Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def dominantIndex(self, nums: List[int]) -> int:
...         max_value1=max(nums)
...         max_index=nums.index(max(nums))
...         nums.remove(max(nums))
...         max_value2=max(nums)
...         if max_value1>=2*max_value2:
...             return max_index
...         else:
...             return -1
