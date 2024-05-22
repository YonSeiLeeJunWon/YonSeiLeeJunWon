Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def equalPairs(self, grid: List[List[int]]) -> int:
...         count=0
...         column=[]
...         for i in range(len(grid[0])):
...             lst=[]
...             for j in range(len(grid[0])):
...                 lst.append(grid[j][i])
...             column.append(lst)
...         for i in grid:
...             for j in column:
...                 if i==j:
...                     count+=1
...         
...         return count
