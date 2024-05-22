Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def isMonotonic(self, nums: List[int]) -> bool:
...         increasing=nums.copy()
...         decreasing=nums.copy()
...         increasing.sort()
...         decreasing.sort(reverse=True)
...         if increasing==nums or decreasing==nums:
...             return True
...         else:
...             return False
