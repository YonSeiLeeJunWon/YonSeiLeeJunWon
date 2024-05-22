Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
...         result=[]
...         items=nums1+nums2
...         id=[]
...         for i in items:
...             if i[0] not in id:
...                 id.append(i[0])
...         id.sort()
...         for i in id:
...             value=0
...             for j in items:
...                 if j[0]==i:
...                     value+=j[1]
...             result.append([i,value])
...         return result
...             
...         
