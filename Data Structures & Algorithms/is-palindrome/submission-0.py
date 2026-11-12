class Solution:
    def isPalindrome(self, s: str) -> bool:

        text =""
        for c in "".join(s.split()):
           if c.isalnum():
            text += c.lower()
        left = 0
        right = len(text)-1
        while left<right:
            if text[left] == text[right]:
                left+=1
                right-=1
            else:
                return False
        return True