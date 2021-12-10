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

    # sort so that x2>=x1, y2>=y1
    if x2<x1:
        x2,x1=x1,x2
    if y2<y1:
        y2,y1=y1,y2

    if (x1==x2):
        for j in range(y1,y2+1):
            field[x1][j]+=1

    if (y1==y2):
        for i in range(x1,x2+1):
            field[i][y1]+=1
count=0
for line in field:
    for cell in line:
        if cell>1:
            count+=1

print(count)
