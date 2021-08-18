class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0 for i in range(len(s)+1)] # initializig our dp
        dp[0]=1 
        dp[1]= 0 if s[0]=='0' else 1 # now the string of only character would result in a letter only when it is not zero so implementing that
        for i in range(2,len(s)+1): # loop for the letter from one to length of s
            oneDigit = s[i-1:i] # taking the condition of one digit
            twoDigit = s[i-2:i] # taking the condition for two digits
            if int(oneDigit)>=1: #here the digit would result in a letter only when greater than on equal to one
                dp[i]+=dp[i-1] #summing up the previous one digit results
            if int(twoDigit)>=10 and int(twoDigit)<=26: #here checking where it may have a two digit or not
                dp[i]+=dp[i-2] #summing up the previous two digit results

        return dp[len(s)] # returning the result for string length