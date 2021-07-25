class Solution:
    def convert(self,s: str, n: int) -> str:
        if n==1:
            return s
        l=len(s)
        arr=["" for i in range(n)]
        row=0
        for i in range(l):
            arr[row]+=s[i]
            if row==0:
                down =True
            elif row==n-1:
                down=False
            if down:
                row+=1
            else:
                row-=1
        return "".join(arr)
def main():
    print(Solution.convert("PAYPALISHIRING",4))
if __name__=="__main__":
    main()