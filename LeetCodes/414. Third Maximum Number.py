Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def thirdMax(self, nums: List[int]) -> int:
...         max_nums=set()
...         
...         for num in nums:
...             max_nums.add(num)
...             if len(max_nums)>3:
...                 max_nums.remove(min(max_nums))
...         
...         if len(max_nums)<3:
...             return max(max_nums)
...         else:
...             return min(max_nums)
