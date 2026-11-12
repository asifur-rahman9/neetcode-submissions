class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        #hybab

        n = len(s)
        longest = ''

        for i in range(n):
            #odd length

            left = i
            right = i
            print(i)
            while left >= 0 and right < n and s[left] == s[right]:
                res = s[left:right+1]
                if len(longest) < len(res):
                    longest = res
                right +=1
                left -=1

            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                res = s[left:right+1]
            
                if len(longest) < len(res):
                    longest = res
                right += 1
                left -= 1
                
                
                
        
        return longest


