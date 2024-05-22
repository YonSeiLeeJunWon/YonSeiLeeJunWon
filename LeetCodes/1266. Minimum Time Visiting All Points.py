Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
...         total=0
...         for i in range(len(points)-1):
...             x1,y1=points[i]
...             x2,y2=points[i+1]
...             total+=max(abs(x2-x1),abs(y2-y1))
...         return total
