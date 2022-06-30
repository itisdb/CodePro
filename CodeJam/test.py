import itertools

a = [1, 2, 3]
n = 3

perm_iterator = itertools.combinations(a,2)

for item in perm_iterator:
    print(item)