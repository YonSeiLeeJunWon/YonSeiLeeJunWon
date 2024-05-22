Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def trimMean(self, arr: List[int]) -> float:
...         length=len(arr)
...         for _ in range(int(length/20)):
...             arr.remove(min(arr))
...             arr.remove(max(arr))
...         total=0
...         for i in arr:
...             total+=i
...         return total/len(arr)
