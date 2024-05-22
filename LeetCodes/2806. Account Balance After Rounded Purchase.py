Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
...         if int(str(purchaseAmount)[-1])>=5:
...             purchaseAmount=purchaseAmount+1
...         else:
...             purchaseAmount-=1
...         return 100-round(purchaseAmount,-1)
