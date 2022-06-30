inp = list(input())
enc = input()

p = 0
for i in range(len(enc)):
    if p<0 or p>=len(inp):
        continue
    if enc[i] in ['0','1','2','3','4','5','6','7','8','9']:
        continue
    if enc[i]=='L':
        if p>0:
            p-=1
    elif enc[i]=='R':
        if p<len(inp)-1:
            p+=1
    elif enc[i]=='T':
        if int(inp[p])<9:
            n=int(inp[p])
            n+=1
            inp[p]=str(n)            
    elif enc[i]=='D':
        if int(inp[p])>0:
            n=int(inp[p])
            n-=1
            inp[p]=str(n)
    elif enc[i]=='S':
        temp=inp[p]
        inp[p]=inp[int(enc[i+1])-1]
        inp[int(enc[i+1])-1]=temp
print(str(''.join(inp)))