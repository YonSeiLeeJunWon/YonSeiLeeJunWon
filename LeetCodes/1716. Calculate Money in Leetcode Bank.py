class Solution:
    def totalMoney(self, n: int) -> int:
        sub_total=0
        s_total=0
        if n//7>1:
            for i in range(2,n//7+1):
                s_total=s_total+7*(i-1)

        for i in range(1,n%7+1):
            sub_total=sub_total+i+(n//7)
        return 28*(n//7)+s_total+sub_total
    
