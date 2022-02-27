def find(matrix):
    zero ={
        'rows': [],
        'cols': []
    }
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]==0:
                if row not in zero['rows']:
                    zero['rows'].append(row)
                if col not in zero['cols']:
                    zero['cols'].append(col)
                break
    return zero

def convert(matrix, zero):
    res = []
    for row in range(len(matrix)):
        r=[]
        for col in range(len(matrix[row])):
            if row in zero['rows'] or col in zero['cols']:
                r.append(0)
            else:
                e = matrix[row][col]
                r.append(e)
        res.append(r)
    return res

def stringtoList(matrix):
    res=[]
    row=[]
    for i in matrix[1:len(matrix)-1]:
        if i=="[" or i==",":
            continue
        elif i=="]":
            res.append(row)
            row=[]
        else:
            row.append(int(i))
    return res

matrix = stringtoList(input())

print(convert(matrix,find(matrix)))