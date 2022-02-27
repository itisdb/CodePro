from itertools import permutations

def nextPerm(matrix):
    s = sorted(matrix)
    allPerm = list(permutations(s))
    print(allPerm)
    for i in range(len(allPerm)):
        if matrix == allPerm[i]:
            print(allPerm[i+1])
            break

matrix = (1,3,2)
nextPerm(matrix)
# print(list(permutations(matrix)))