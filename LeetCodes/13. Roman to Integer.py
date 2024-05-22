Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def romanToInt(self, s: str) -> int:
...         roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
...         result=0
...         prev_value=0
...         for char in s:
...             value=roman_values[char]
...             if value>prev_value:
...                 result+=value-2*prev_value
...             else:
...                 result+=value
...             prev_value=value
...         return result
... 
...     
