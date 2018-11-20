def Fib(row,col):
    out=[]
    
    rowCount = 0
    colCount = 1
    for x in range(row):
        newRow = []
        
        for y in range(col):
            if x == 0 and y ==0:
                newRow.append(0)
            elif x ==0 and y==1:
                newRow.append(1)
            else:
                newRow.append(rowCount + colCount)
                rowCount = colCount 
                colCount = newRow[y]
        out.append(newRow)
        
    return out
pattern = Fib(5,15)
for row in pattern:
    print(row)