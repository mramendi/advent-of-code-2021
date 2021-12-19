import ast
baseNnumerals="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ"
N=len(baseNnumerals)
def baseN(n):
    '''
    convert a number to a baseN digit
    '''
    if (n<0) or (n>=N):
        raise IndexError
    return baseNnumerals[n]

def debaseN(c):
    '''
    convert a single baseN digit to a number
    '''
    n=baseNnumerals.find(c)
    if n==-1:
        raise IndexError
    return n

def locate_number_left(numstring,cursor):
    '''
    locate nearest baseN number to the left of cursor, return position
    return -1 if there is none
    cursor location not included
    '''
    pos=cursor-1
    while pos>=0:
        if numstring[pos].isalnum():
            return pos
        pos-=1
    return -1

def locate_number_right(numstring,cursor):
    '''
    locate nearest base20 number to the right of cursor, return position
    return -1 if there is none
    cursor location not included
    '''
    pos=cursor+1
    while pos<len(numstring):
        if numstring[pos].isalnum():
            return pos
        pos+=1
    return -1


def reduce_number_once(numstring):
    '''
    "reduce" a number string exactly once
    return a tuple (numstring, reduced) where reduced is boolean, true if number was modified
    '''
    cursor = 0
    depth = 0
    # explode first
    while cursor < len(numstring):
        if numstring[cursor]=="[":
            depth+=1
            cursor+=1
            continue
        if numstring[cursor]=="]":
            depth-=1
            cursor+=1
            continue
        # now we are facing a base 20 number or comma at the cursor
        if depth>4:
#            print(numstring)
            # we are at the start of a pair within >4 pairs
            num1=debaseN(numstring[cursor])
            # numstring[cursor+1] is a comma
            num2=debaseN(numstring[cursor+2])
            left_number_pos=locate_number_left(numstring,cursor)
            if left_number_pos>=0:
                old_left=debaseN(numstring[left_number_pos])
                new_num_left=numstring[:left_number_pos]+baseN(old_left+num1)+numstring[left_number_pos+1:cursor-1]
            else:
                new_num_left=numstring[:cursor-1]
            if cursor+4>=len(numstring):
                new_num_right=""
            else:
                right_number_pos=locate_number_right(numstring,cursor+4)
                if right_number_pos>=0:
                    old_right=debaseN(numstring[right_number_pos])
                    new_num_right=numstring[cursor+4:right_number_pos]+baseN(old_right+num2)+numstring[right_number_pos+1:]
                else:
                    new_num_right=numstring[cursor+4:]
#            print(new_num_left)
#            print(new_num_right)
            return(new_num_left+"0"+new_num_right,True)
        cursor+=1

    # split next
    cursor=0
    while cursor < len(numstring):
        if numstring[cursor].isalpha():
            # this means we have a digit that is over 9
            num=debaseN(numstring[cursor])
            num1=num//2
            num2=num//2+num%2
            return (numstring[:cursor]+"["+baseN(num1)+","+baseN(num2)+"]"+numstring[cursor+1:],True)
        cursor+=1
    return(numstring,False)

def reduce_number(numstring):
    '''
    reduce a number fully as per instructions
    '''
    newnum=numstring
    reduced=True
    while reduced:
        newnum,reduced=reduce_number_once(newnum)
    return newnum

def magnitude(subj_s):
    subj=subj_s
    if isinstance(subj_s,str):
        subj=ast.literal_eval(subj_s)
    if isinstance(subj,int):
        return subj
    if isinstance(subj,list):
        if len(subj)!=2:
            print("WRONG LIST: ",subj)
            raise IndexError
        return 3*magnitude(subj[0])+2*magnitude(subj[1])


f=open("input18.txt").readlines()
num=f[0].strip()
ln=1
num=reduce_number(num)
while ln<len(f):
    if f[ln].strip=="":
        break
    num="["+num+","+f[ln].strip()+"]"
    num=reduce_number(num)
    ln+=1

print ("Part 1:",magnitude(num))

max_magnitude=0
for i in range(0,len(f)):
    for j in range(0,len(f)):
        if i==j:
            continue
        num="["+f[i].strip()+","+f[j].strip()+"]"
        num=reduce_number(num)
        mag=magnitude(num)
        if mag>max_magnitude:
            max_magnitude=mag

print("Part 2:",max_magnitude)
