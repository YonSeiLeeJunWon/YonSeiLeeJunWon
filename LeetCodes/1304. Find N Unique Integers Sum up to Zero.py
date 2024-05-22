Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def sumZero(self, n: int) -> List[int]:
        Lst=[]
        if n % 2 == 0:
            for i in range(1, n // 2 + 1):
                Lst.append(i)
                Lst.append(-i)
            return Lst
        else:
            Lst.append(0)
            for i in range(1, n // 2 + 1):
                Lst.append(i)
                Lst.append(-i)
            return Lst

        

