# just for definition
xmin=0
xmax=0
ymin=0
ymax=0

MAXTRY = 1000

def step(state):
    '''step of the trajectory
    state is a tuple (x,y,vx,vy)
    returns a similar tuple
    '''
    x,y,vx,vy=state
    x=x+vx
    y=y+vy
    if vx>0:
        vx-=1
    elif vx<0: # just for completeness
        vx+=1
    vy-=1
    return (x,y,vx,vy)

def fire(vx,vy):
    '''result of firing from 0,0 with vx/vy velocities
    returns:
    >=0 - max y if target area was hit
    -1 if, by y<ymin, we still have x<xmin (never reached horizontally)
    -2 if, by y<ymin, x>xmin, but target was never hit ("overstepped")
    -3 if, by x>xmax, y>ymax (overreached horizontally)
    '''
    state=(0,0,vx,vy)
    max_y=0
    while True:
        state=step(state)
        x,y,new_vx,new_vy=state
        if y>max_y:
            max_y=y
        if (x<=xmax) and (x>=xmin) and (y<=ymax) and (y>=ymin):
            return max_y
        if (y>ymax) and (x>xmax):
            return -3
        if y<ymin:
            if x<xmin:
                return -1
            return -2

s=open("input17.txt").readlines()[0]
throwaway,rest1,rest2=s.split("=")
s_xmin,rest1_1=rest1.split("..")
s_xmax,throwaway=rest1_1.split(",")
s_ymin,rest1_1=rest1.split("..")
s_ymin,s_ymax=rest2.split("..")
s_ymax=s_ymax.strip()
xmin=int(s_xmin)
xmax=int(s_xmax)
ymin=int(s_ymin)
ymax=int(s_ymax)

max_y=0
count=0
for vy in range(ymin,MAXTRY):
    vx=1
    while True:
        result=fire(vx,vy)
        if result>=0:
            count+=1
        if result>max_y:
            max_y=result
        if result==-3:
            break # an overshot ends the loop
        if vx>=xmax:
            break # with vx>max_x we can't hit the area, guaranteed overshot
        vx+=1

print ("Part 1:", max_y)
print ("Part 2:", count)
