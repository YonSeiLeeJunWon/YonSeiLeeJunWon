class Solution:
    def interpret(self, command: str) -> str:
        command1=command.replace("()","o")
        command2=command1.replace("(al)","al")
        return command2
    
