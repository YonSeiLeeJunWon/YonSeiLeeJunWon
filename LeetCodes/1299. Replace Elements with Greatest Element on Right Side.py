Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def replaceElements(self, arr: List[int]) -> List[int]:
...         for i in range(len(arr)-1):
...             if i==0 or arr[i-1]==arr[i]:
...                 arr[i]=max(arr[i+1:len(arr)])
...             else:
...                 arr[i]=arr[i-1]
...         arr[len(arr)-1]=-1
...         return arr
