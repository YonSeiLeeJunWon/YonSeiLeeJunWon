Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
...         lst=[]
...         for i in nums1:
...             if i in nums2 or i in nums3:
...                 lst.append(i)
...         for j in nums2:
...             if j in nums3:
...                 lst.append(j)
...         return list(set(lst))
