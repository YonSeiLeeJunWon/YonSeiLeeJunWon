Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def isPalindrome(self, s: str) -> bool:
...         p=""
...         alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
...         ALPHA=["A","B","C","D",'E',"F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
...         num=["0","1","2","3","4","5","6","7","8","9"]
...         for i in range(0,len(s)):
...             if s[i] in alpha:
...                 p=p+s[i]
...             elif s[i] in ALPHA:
...                 s=s.lower()
...                 p=p+s[i]
...             elif s[i] in num:
...                 p=p+s[i]
...             i=i+1
...         if p[0:]==p[-1::-1]:
...             return True
...         else:
...             return False
