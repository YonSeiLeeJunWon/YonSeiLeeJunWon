Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def convertTemperature(self, celsius: float) -> List[float]:
...         a=[]
...         Kel=celsius + 273.15
...         Fah=celsius * 1.80 + 32.00
...         a.append(Kel)
...         a.append(Fah)
...         return a
