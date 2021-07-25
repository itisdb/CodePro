class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''here we will be using window sliding'''
        # for reference please go to : https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

        n=len(s)
        count=0
        for i in range(n):
            visited=[0]*256
            for j in range(i,n):
                if visited[ord(s[j])]==True:
                    break
                else:
                    visited[ord(s[j])]=True
                    count=max(count,j-i+1)
            visited[ord(s[j])]=False
        return count
