# THIS DOES NOT WORK - takes too long on a working input; some debug output is in, Saved for history only

# NOTES:
# x is vertical and y is horizontal - just easier in Python
# paths and path_sums are global lists of paths (as list-of-tuples)
#   and corresponding sums. They are globals because I am lazy.
#   Sums in path_sums INCLUDE the starting point!
#   Have to correct this when printing
# size is the size of the square and is also global
paths = []
path_sums = []
minimum_sum=10000000 # "way too much"
size = 10 # here just for definition, actual size determined when parsing input
len_excl=0
loop_excl=0
adjacents = [(0,1),(0,-1),(1,0),(-1,0)]

def walk_new_point(path_so_far, sum_so_far, new_point):
    ''' Recursive walk to a new point - checking if it is eligible too

    Parameters:
    path_so_far - list of tuples for the path NOT including the new point
    sum_so_far - sum for the path NOT including the new point
    new_point - x,y tuple for the new point
    '''
#    print (new_point)

    global paths, path_sums, minimum_sum, len_excl, loop_excl

    if len(path_so_far) > 3*size:
        len_excl+=1
        if len_excl%100==0:
            print("Length excluded:",len_excl)
        return # a guesstimate? avoids max recursion depth errors too
    if sum_so_far >= minimum_sum:
        return
        print("Sum exceeded")


    if new_point == (size-1,size-1):
        # reached the endpoint; add the path to global list and return
        if (path_so_far+[new_point]) in paths:
            print ("DUPLICATE",path_so_far+[new_point])
        paths.append(path_so_far+[new_point])
        new_sum=sum_so_far+field[size-1][size-1]
        path_sums.append(sum_so_far+field[size-1][size-1])
        if new_sum < minimum_sum:
            minimum_sum = new_sum

        # This works as a progress indicator to ensure no endless loop
        #if len(path_sums)%20 == 0:
        print("Paths found:",len(path_sums))
#        print (path_so_far+[new_point])

    x,y = new_point

    if len(path_so_far) > 0:
        last_point = path_so_far[-1]
        # check the new point for eligibility
        # if it is adjacent to any point in the path except the last one, return
        # to do this we loop through all four adjacent points, no need to check bounds
        # NOTE checks might be taking too long
        for si,sj in adjacents:
            i,j=x+si,y+sj
            if (i,j) == last_point:
                continue
            if (i,j) in path_so_far:
                loop_excl+=1
#                if loop_excl%100==0:
#                    print("Loop excluded:",loop_excl,len_excl,len(path_so_far))
                return
    else:
        last_point = (-10,-10) # for an empty path create an irrelevant last point


    # the new point is eligibLe to be added to the path if we are here
    # so we create a path and sum with it, then walk to all adjacent points
    #  except, of course, the one we came here from
    new_path_so_far = path_so_far+[new_point]
    new_sum_so_far = sum_so_far+field[x][y]

    for si,sj in adjacents:
        i,j=x+si,y+sj
        if (i<0) or (i>=size) or (j<0) or (j>=size) or ((i,j)==last_point):
                continue
        walk_new_point(new_path_so_far, new_sum_so_far, (i,j))

f = open("input15.txt").readlines()
field=[]
for s in f:
    if s.strip()=="": continue
    line=[int(chr) for chr in s.strip()]
    field.append(line)
size = len(field)
if len(field[0]) != size:
    print("WARNING: not really a square?")

# Seed the minimum_sum with a fixed path
minimum_sum = 0
for i in range(0,size):
    minimum_sum+=field[i][0]
for j in range(1,size):
    minimum_sum+=field[size-1][j]


walk_new_point([],0,(0,0))
print (minimum_sum-field[0][0])
