Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
        return count
    
