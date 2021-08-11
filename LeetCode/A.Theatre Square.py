import math
class Solution:
    def theatreSquare(self,n,m,a):
        if n==0 or m==0 or a==0:
            return 0
        else:
            if n%a==0 and m%a==0:
                return (n*m)//(a*a)
            else:
                n=math.ceil(n/a)*a
                m=math.ceil(m/a)*a
                return (n*m)//(a*a)
                
    def main(self):
        n=input()
        s=n.split(' ')
        print(self.theatreSquare(int(s[0]),int(s[1]),int(s[2])))

if __name__ == '__main__':
    Solution().main()