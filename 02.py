f = open("input2.txt").readlines()
depth = 0
horiz = 0
for s in f:
    [cmd,sn]=s.split()
    n=int(sn)
    if cmd=="forward":
        horiz+=n
    if cmd=="down":
        depth+=n
    if cmd=="up":
        depth-=n
print(horiz*depth)

depth = 0
horiz = 0
aim = 0
for s in f:
    [cmd,sn]=s.split()
    n=int(sn)
    if cmd=="forward":
        horiz+=n
        depth+=(n*aim)
    if cmd=="down":
        aim+=n
    if cmd=="up":
        aim-=n
print(horiz*depth)
