class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flip=0
        bin1=str(bin(start))[2:]
        bin2=str(bin(goal))[2:]
        if len(bin1)<len(bin2):
            while len(bin1)<len(bin2):
                bin1="0"+bin1
        elif len(bin1)>len(bin2):
            while len(bin1)>len(bin2):
                bin2="0"+bin2
        for i in range(0,len(bin1)):
            if bin1[i]!=bin2[i]:
                flip+=1
        return flip
    
