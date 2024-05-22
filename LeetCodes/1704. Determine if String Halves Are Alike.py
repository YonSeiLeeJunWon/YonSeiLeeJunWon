Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def halvesAreAlike(self, s: str) -> bool:
...         count_a=0
...         count_b=0
...         vowels=['a','e','i','o','u','A','E','I','O','U']
...         for i in s[0:int(len(s)/2)]:
...             if i in vowels:
...                 count_a+=1
...         for j in s[int(len(s)/2):len(s)]:
...             if j in vowels:
...                 count_b+=1
...         if count_a==count_b:
...             return True
...         else:
...             return False
