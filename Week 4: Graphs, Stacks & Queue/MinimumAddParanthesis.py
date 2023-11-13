class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        output=[]
        for i in range(len(s)):
            if s[i] == '(':
                output.append(s[i])
            elif s[i]==')':
                output.pop() if output and output[-1]=='(' else output.append(s[i])
        return len(output)
        
