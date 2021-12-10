def most_common_bit(lines,pos): # if the numbers of 0 and 1 are equal, return 1
    count_ones=0
    for s in lines:
        if s[pos]=="1":
            count_ones+=1
    if count_ones >= (len(lines)/2):
        return ("1")
    else:
        return ("0")

f = open("input3.txt").readlines()
number_of_bits=len(f[0].strip()) # we do assume same length of all input lines
ones={}
for i in range(0,number_of_bits):
    ones[i]=0
for s in f:
    for i in range(0,number_of_bits):
        if s[i]=="1":
            ones[i]+=1
        elif s[i]!="0": #sanity check
            print("ERROR")

gamma=""
epsilon=""
cutoff=len(f)/2
for i in range(0,number_of_bits):
    if ones[i] > cutoff:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"
print (int(gamma,2)*int(epsilon,2))

# find oxygen rating
curr_f = f.copy()
for i in range(0,number_of_bits):
    mcb = most_common_bit(curr_f,i)
    new_f=[]
    for s in curr_f:
        if s[i]==mcb:
            new_f.append(s)
    curr_f=new_f
    if len(curr_f)==1:
        break
if len(curr_f)!=1:
    print("ERROR in oxygen")
oxygen=int(curr_f[0],2)

# find co2 rating
curr_f = f.copy()
for i in range(0,number_of_bits):
    mcb = most_common_bit(curr_f,i)
    lcb = "1" if mcb=="0" else "0"
    new_f=[]
    for s in curr_f:
        if s[i]==lcb:
            new_f.append(s)
    curr_f=new_f
    if len(curr_f)==1:
        break
if len(curr_f)!=1:
    print("ERROR in co2")
co2=int(curr_f[0],2)

print(oxygen*co2)
