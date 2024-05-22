class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet=set('abcdefghijklmnopqrstuvwxyz')
        return len(set(sentence))>=len(alphabet)
    
