Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def finalPrices(self, prices: List[int]) -> List[int]:
...         discount=0
...         result=[]
...         for i in range(len(prices)-1):
...             for j in range(i+1,len(prices)):
...                 if prices[i]>=prices[j]:
...                     discount=prices[j]
...                     break
...             result.append(prices[i]-discount)
...             discount=0
...         result.append(prices[len(prices)-1])
...         return result
