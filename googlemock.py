arr = [1,0,3,0,5]
prod=1
checkZero = False

for i in arr:
    if i == 0:
        checkZero = True
    else:
        prod *= i

prodres =[]
for i in arr:
    if checkZero:
        if i == 0:
            prodres.append(prod)
        else:
            prodres.append(0)
    else:
        prodres.append(prod//i)

print(prodres)