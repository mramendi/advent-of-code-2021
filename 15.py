
# NOTES:
# x is vertical and y is horizontal - just easier in Python

adjacents = [(0,1),(0,-1),(1,0),(-1,0)]
paths = []
path_sums = []
MAXINT=10000000000 # "way too much"
size = 10 # here just for definition, actual size determined when parsing input



f = open("input15.txt").readlines()
field=[]
for s in f:
    if s.strip()=="": continue
    line=[int(chr) for chr in s.strip()]
    field.append(line)
size = len(field)
if len(field[0]) != size:
    print("WARNING: not really a square?")

updated={(0,0):0}
spt={}
minimums_cache_stack=[(0,(0,0))]

while len(updated)>0:
    current_coord=None
    current_risk=MAXINT
    # attempt to recover the minimum from the cache stack
    try:
        # uncomment the next line to NOT use caching
        # raise IndexError
        risk,coord=minimums_cache_stack.pop()
        if updated[coord]!=risk:
            raise IndexError
        current_coord=coord
        current_risk=risk
        if current_risk>min(updated.values()):
            print("BUG",current_risk,min(updated.values()))
    except (IndexError,KeyError):
        # cache stack is empty or invalid, nullify it and find the minimum
        current_risk=min(updated.values())
        minimums_cache_stack=[]
        current_risk_index=list(updated.values()).index(current_risk)
        current_coord=list(updated.keys())[current_risk_index]

    x,y = current_coord
    # the current minimum for pushing into stack
    if len(minimums_cache_stack)==0:
        current_minimum=min(updated.values())
    else:
        current_minimum,temp_coord=minimums_cache_stack[-1]
    # update all neighbouts except those already in spt
    for si,sj in adjacents:
        i,j=x+si,y+sj
        if (i<0) or (i>=size) or (j<0) or (j>=size) or ((i,j) in spt):
            continue
        new_risk=MAXINT
        try:
            new_risk=updated[(i,j)]
        except KeyError:
            pass
        candidate_risk=current_risk+field[i][j]
        if candidate_risk<new_risk:
            updated[(i,j)]=candidate_risk
            # if this is smaller than, or equal to, the current minimum, push to cache stack
            if candidate_risk<=current_minimum:
                minimums_cache_stack.append((candidate_risk,(i,j)))
                current_minimum=candidate_risk
    # add the current coord to spt
    spt[current_coord]=current_risk
    # remove the current coord from updated
    del updated[current_coord]

    # if we reached the bottom right we're done
    if current_coord==(size-1,size-1):
        break

print (spt[(size-1,size-1)])
