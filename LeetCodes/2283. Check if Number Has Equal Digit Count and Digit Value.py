class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        for i in range(n):
            count = num.count(str(i))
            if count != int(num[i]):
                return False
        return True
    
