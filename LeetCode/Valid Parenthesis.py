class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not stack
