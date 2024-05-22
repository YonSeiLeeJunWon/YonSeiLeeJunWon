Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def mostFrequentEven(self, nums: List[int]) -> int:
...         nums.sort(reverse=True)
...         dic={}
...         for i in nums:
...             if i%2==0:
...                 if i not in dic:
...                     dic[i]=1
...                 else:
...                     dic[i]+=1
...         max_value=-1
...         result=-1
...         for i, j in dic.items():
...             if j>=max_value:
...                 max_value=j
...                 result=i
...         return result
