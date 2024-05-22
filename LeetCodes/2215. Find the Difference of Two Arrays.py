Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
...         ans=[]
...         lst1=[]
...         lst2=[]
...         for i in range(len(nums1)):
...             if nums1[i] not in nums2:
...                 if nums1[i] not in lst1:
...                     lst1.append(nums1[i])
...         for i in range(len(nums2)):
...             if nums2[i] not in nums1:
...                 if nums2[i] not in lst2:
...                     lst2.append(nums2[i])
...         ans.append(lst1)
...         ans.append(lst2)
...         return ans
