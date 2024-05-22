Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def checkValid(self, matrix: List[List[int]]) -> bool:
...         lst=[]
...         for i in range(1,len(matrix)+1):
...             lst.append(i)
...         #row
...         for i in matrix:
...             for j in lst:
...                 if j not in i:
...                     return False
...         #column
...         for j in range(len(matrix)):
...             column_lst=[]
...             for i in range(len(matrix)):
...                 column_lst.append(matrix[i][j])
...             for k in lst:
...                 if k not in column_lst:
...                     return False
... 
...         return True
