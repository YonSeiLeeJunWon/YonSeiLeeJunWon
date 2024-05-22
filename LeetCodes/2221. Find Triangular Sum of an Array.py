Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def triangularSum(self, nums: List[int]) -> int:
...         while len(nums) > 1:
...             new_nums=[(nums[i]+nums[i+1])%10 for i in range(len(nums) - 1)]
...             nums = new_nums
...         return nums[0]
