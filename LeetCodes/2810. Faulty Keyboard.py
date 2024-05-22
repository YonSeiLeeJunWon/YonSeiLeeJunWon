class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for i in s:
            if i=="i":
                left=0
                right=len(result)-1
                while left < right:
                    result[left], result[right] = result[right], result[left]
                    left += 1
                    right -= 1
            else:
                result.append(i)
        return ''.join(result)
    
