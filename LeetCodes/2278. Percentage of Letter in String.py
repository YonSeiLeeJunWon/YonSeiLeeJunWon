class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total=0
        event=0
        for i in s:
            if i==letter:
                total+=1
                event+=1
            else:
                total+=1
        return int(event/total*100)
    
