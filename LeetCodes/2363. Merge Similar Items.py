Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
...         result=[]
...         for i in items1:
...             weight2=0
...             weight1=i[1]
...             for j in items2:
...                 if j[0]==i[0]:
...                     weight2=j[1]
...             result.append([i[0],weight1+weight2])
... 
...         for i in items2:
...             weight1=0
...             weight2=i[1]
...             for j in items1:
...                 if j[0]==i[0]:
...                     weight1=j[1]
...             if [i[0],weight1+weight2] not in result:
...                 result.append([i[0],weight1+weight2])
... 
...         while True:
...             count=0
...             for i in range(1,len(result)):
...                 if (result[i])[0]<(result[i-1])[0]:
...                     count+=1
...                     result[i-1], result[i] = result[i], result[i-1]
...             if count==0:
...                 break
...         return result
