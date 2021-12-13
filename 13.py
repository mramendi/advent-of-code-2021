def fold_x(n,field):
    new_field=set()
    for x,y in field:
        if x<n:
            new_field.add((x,y))
        elif x>n:
            if 2*n-x<0:
                print("WARNING: FOLD RESULTED IN NEGATIVE COORDINATE X")
            new_field.add((2*n-x,y))
        else:
            print("WARNING: DOT ON FOLD LINE X")
    return new_field

def fold_y(n,field):
    new_field=set()
    for x,y in field:
        if y<n:
            new_field.add((x,y))
        elif y>n:
            if 2*n-y<0:
                print("WARNING: FOLD RESULTED IN NEGATIVE COORDINATE Y")
            new_field.add((x,2*n-y))
        else:
            print("WARNING: DOT ON FOLD LINE Y")
    return new_field

def print_field(field):
    # to print out the resulting matrix we first need its dimensions
    max_x = 0
    max_y = 0
    for x,y in field:
        if x>max_x: max_x=x
        if y>max_y: max_y=y

    # now we can print out the matrix
    for y in range(max_y+1):
        s=""
        for x in range(max_x+1):
            if (x,y) in field:
                s+="#"
            else:
                s+=" "
        print(s)
    print()

field=set()
f = open("input13.txt").readlines()
index_line=0
while f[index_line].strip()!="":
    sx,sy=f[index_line].strip().split(",")
    field.add((int(sx),int(sy)))
    index_line+=1

index_line+=1
part_one_printed = False
while index_line<len(f):
    cmd,sn=f[index_line].strip().split("=")
    n=int(sn)
    if cmd[-1]=="x":
        field=fold_x(n,field)
    elif cmd[-1]=="y":
        field=fold_y(n,field)
    else:
        print("WARNING: UNRECOGNIZED COMMAND")
    index_line+=1
    if not part_one_printed:
        print("Part 1: ",len(field))
        part_one_printed = True

print_field(field)
