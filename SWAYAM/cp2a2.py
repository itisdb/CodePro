N = int(input()) # number of people
a = list(map(int, input().split()[:N])) #vibe value input
a = sorted(a, reverse=True) # sort in descending order
def find(a:list):
    index = 0
    m = 0
    for i in range(0, len(a)-1):
        if min(a[i], a[i+1]) > m:
            m = min(a[i], a[i+1])
            index = i
    return [index,m]

studyGroup = [] #studygroup list
studyGroup.append(a[0]) #add first value to list
goodVibes = studyGroup[0] #good vibes
for i in a[1:]:
    f = find(studyGroup)
    goodVibes += f[1]
    studyGroup.insert(f[0]+1, i)

print(goodVibes,end='')

