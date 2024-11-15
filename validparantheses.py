class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in pairs:  # If it's an opening bracket
                stack.append(char)
            elif stack and pairs[stack[-1]] == char:  # If it's a matching closing bracket
                stack.pop()
            else:
                return False  # If it doesn't match, it's invalid

        return not stack   
