Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... class Solution:
...     def diagonalSum(self, mat: List[List[int]]) -> int:
...         if len(mat)%2==0:
...             total=0
...             j=0
...             for i in mat:
...                 total+=i[j]+i[len(mat)-j-1]
...                 j+=1
...         else:
...             total=0
...             j=0
...             for i in mat:
...                 if j==len(mat)-j-1:
...                     total+=i[j]
...                 else:
...                     total+=i[j]+i[len(mat)-j-1]
...                 j+=1
...         return total
...             
