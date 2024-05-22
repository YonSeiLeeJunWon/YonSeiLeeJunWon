Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def buyChoco(self, prices: List[int], money: int) -> int:
...         price=0
...         for _ in range(2):
...             price+=min(prices)
...             prices.remove(min(prices))
...         if price>money:
...             return money
...         else:
...             return money-price
