Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
...         count=0
...         vowel_list=["a","e","i","o","u"]
...         for i in range(left,right+1):
...             if (words[i])[0] in vowel_list and (words[i])[len(words[i])-1] in vowel_list:
...                 count+=1
...         return count
