class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for i in range(1,n+1):
            for j in range(i,n+1):
                if i**2+j**2<=n*n and int((i**2+j**2)**0.5) ==(i**2+j**2)**0.5:
                    if i!=j:
                        count+=2
                    else:
                        count+=1
        return count
    
