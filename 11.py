import pprint

neighbour_offsets=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

gridsize = 10

f = open("input11.txt").readlines()
field=[]
for s in f:
    if s.strip()=="": continue
    line=[int(chr) for chr in s.strip()]
    field.append(line)
#pprint.pprint(field)

flashes_total=0
part2_done=False
for step in range(10000):
    flashed=set()
    flashes_this_step=0

    # walk field, increase energy by 1, find initial flashes
    # NOTE: after this walk, and at further stages, a leve of 0 means "flashed", not to be increased until next step
    for i in range(gridsize):
        for j in range(gridsize):
            field[i][j]+=1
            if field[i][j]>9:
                field[i][j]=0
                flashed.add((i,j))

    flashes_this_step += len(flashed)
    flashed_previous_iteration=flashed
    while len(flashed_previous_iteration)>0:
#        pprint.pprint(field)
        flashed_new_iteration=set()
        for (i,j) in flashed_previous_iteration:
            for offset in neighbour_offsets:
                oi,oj=offset
                ni=i+oi
                nj=j+oj
                if (ni>=0) and (ni<gridsize) and (nj>=0) and (nj<gridsize):
                    if field[ni][nj]==0: continue
                    field[ni][nj]+=1
                    if field[ni][nj]>9:
                        field[ni][nj]=0
                        flashed_new_iteration.add((ni,nj))
        flashes_this_step += len(flashed_new_iteration)
        flashed_previous_iteration = flashed_new_iteration
    flashes_total += flashes_this_step
    if step == 99:
        print("Answer to part 1: "+str(flashes_total))
        if part2_done: break
    if flashes_this_step == 100:
        print("Answer to part 2: "+str(step+1))
        if step >= 99: break
        part2_done = True

#    pprint.pprint(field)

#print(flashes_total)
