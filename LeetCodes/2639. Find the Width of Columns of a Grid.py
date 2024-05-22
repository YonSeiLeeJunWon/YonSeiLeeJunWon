Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
...         lst=[]
...         for j in range(len(grid[0])):
...             col_length=0
...             for i in range(len(grid)):
...                 if col_length<len(str(grid[i][j])):
...                     col_length=len(str(grid[i][j]))
...             lst.append(col_length)
...         return lst
