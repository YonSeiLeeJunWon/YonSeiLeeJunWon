Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
...         result_same=10
...         result_diff=10
...         for i in nums1:
...             if i in nums2 and i<result_same:
...                 result_same=i
...         
...         result_diff=int(str(min(min(nums1),min(nums2)))+str(max(min(nums1),min(nums2))))
... 
...         if result_same==10:
...             return result_diff
...         else:
...             return result_same
