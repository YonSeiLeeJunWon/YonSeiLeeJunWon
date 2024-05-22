Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        count = [True] * n
        count[0] = count[1] = False
        for i in range(2, int(n**0.5) + 1):
            if count[i]:
                for j in range(i*i, n, i):
                    count[j] = False
        return sum(count)
    
