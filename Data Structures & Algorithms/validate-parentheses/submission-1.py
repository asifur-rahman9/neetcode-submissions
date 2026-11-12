class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in paren:
                if stack and stack[-1] == paren[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False




