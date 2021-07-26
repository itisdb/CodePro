class Solution:
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        result = 0
        for i in range(len(s)):
            if s[i] < '0' or s[i] > '9':
                break
            result = result * 10 + ord(s[i]) - ord('0')
        result *= sign
        if result > (pow(2,31)-1):
            return pow(2,31)-1
        if result < -pow(2,31):
            return -pow(2,31)
        return result
