def modified_range(a,b):
    if a>b:
        return range(a,b-1,-1)
    else:
        return range(a,b+1)

max_coord = 1000
field=[]
for i in range(0,max_coord):
    field.append([0]*max_coord)

f = open("input5.txt").readlines()
for s in f:
    [sx1,rs,sy2]=s.strip().split(",")
    [sy1,sx2]=rs.split("->")
    x1=int(sx1)
    x2=int(sx2)
    y1=int(sy1)
    y2=int(sy2)

    if (x1==x2):
        for j in modified_range(y1,y2):
            field[x1][j]+=1
    elif (y1==y2):
        for i in modified_range(x1,x2):
            field[i][y1]+=1
    else:
        # assume diagonal
        y_step=(1 if y1<y2 else -1)
        j=y1
        for i in modified_range(x1,x2):
            field[i][j]+=1
            j+=y_step
count=0
for line in field:
    for cell in line:
        if cell>1:
            count+=1

print(count)
