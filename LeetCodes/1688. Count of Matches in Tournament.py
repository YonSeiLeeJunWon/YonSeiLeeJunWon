class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        while n>=2:
            if n%2==0:
                matches=matches+n/2
                n=n/2
            else:
                matches=matches+(n-1)/2
                n=(n+1)/2
        return int(matches)
    
