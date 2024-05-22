class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>1:
            if n%3!=0 and (n-1)%3!=0:
                return False
            elif n%3==0:
                n=n/3
            else:
                n=(n-1)/3
        return True
    
