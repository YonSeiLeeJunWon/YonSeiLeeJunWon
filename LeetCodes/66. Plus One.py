Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def plusOne(self, digits: List[int]) -> List[int]:
...         num=""
...         plus_num=0
...         lst=[]
...         for i in digits:
...             num=num+str(i)
...         plus_num=int(num)+1
...         for j in str(plus_num):
...             lst.append(int(j))
...         return lst
