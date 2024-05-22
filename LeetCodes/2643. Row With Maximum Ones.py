Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
...         max_index=-1
...         max_value=-1
...         for i in range(len(mat)):
...             value=0
...             for j in mat[i]:
...                 value+=j
...             if max_value<value:
...                 max_value=value
...                 max_index=i
...         return [max_index,max_value]
