Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Lst=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                Lst.append("FizzBuzz")
            elif i%3==0:
                Lst.append("Fizz")
            elif i%5==0:
                Lst.append("Buzz")
            else:
                Lst.append(str(i))
        return Lst
    
