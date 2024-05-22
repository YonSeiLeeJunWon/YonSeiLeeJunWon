class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splited_s=s.split()
        sentence=splited_s[0]
        for i in range(1,k):
            sentence=sentence+" "+splited_s[i]
        return sentence
    
