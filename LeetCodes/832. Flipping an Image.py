Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
...         lst=[]
...         for i in image:
...             i.reverse()
...             for j in range(len(i)):
...                 if i[j]==1:
...                     i[j]=0
...                 else:
...                     i[j]=1
...             lst.append(i)
...         return lst
