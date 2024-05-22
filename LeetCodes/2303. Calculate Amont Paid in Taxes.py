Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def calculateTax(self, brackets: List[List[int]], income: int) -> float:
...         total_tax=0
...         while True:
...             for i in range(len(brackets)):
...                 if i==0:
...                     if income>=brackets[i][0]:
...                         total_tax+=brackets[i][0]*brackets[i][1]/100
...                         income-=brackets[i][0]
...                     else:
...                         total_tax+=income*brackets[i][1]/100
...                         return total_tax
...                 else:
...                     if income>=brackets[i][0]-brackets[i-1][0]:
...                         total_tax+=(brackets[i][0]-brackets[i-1][0])*brackets[i][1]/100
...                         income-=(brackets[i][0]-brackets[i-1][0])
...                     else:
...                         total_tax+=income*brackets[i][1]/100
...                         return total_tax
...                         
... 
