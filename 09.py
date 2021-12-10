field=[]

def errorproof(x,y):
    if (x<0) or (y<0):
        return 15
    try:
        return field[x][y]
    except IndexError:
        return 15

f = open("input9.txt").readlines()
field=[]
for s in f:
    if s.strip()=="": continue
    line=[int(chr) for chr in s.strip()]
    field.append(line)

low_point_sum=0

for i in range(len(field)):
    for j in range(len(field[i])):
        a1=errorproof(i,j-1)
        a2=errorproof(i,j+1)
        a3=errorproof(i+1,j)
        a4=errorproof(i-1,j)
        a0=errorproof(i,j)
        if (a0<a1) and (a0<a2) and (a0<a3) and (a0<a4):
            low_point_sum+=(a0+1)
print(low_point_sum)

basin_sizes=[]
while True:
    #find some starting point
    found=False
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]<9:
                found=True
                field[i][j]=12
                break
        if found: break
    if not found: break

    # do expansion rounds until a round allows no expansion
    while True:
        expanded = 0
        for i in range(len(field)):
            for j in range(len(field[i])):
                if (field[i][j]==12):
                    if errorproof(i,j-1)<9:
                        field[i][j-1]=12
                        expanded+=1
                    if errorproof(i,j+1)<9:
                        field[i][j+1]=12
                        expanded+=1
                    if errorproof(i-1,j)<9:
                        field[i-1][j]=12
                        expanded+=1
                    if errorproof(i+1,j)<9:
                        field[i+1][j]=12
                        expanded+=1
        if expanded==0: break

    # count all instances of 12, replacing them with 13
    size=0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if (field[i][j]==12):
                size+=1
                field[i][j]=13
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)

print (basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
