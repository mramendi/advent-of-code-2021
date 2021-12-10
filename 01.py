f = open("input1.txt").readlines()
count = 0
for i in range(1,len(f)):
    if int(f[i-1])<int(f[i]):
        count+=1
print(count)

count = 0
for i in range(3,len(f)):
    if int(f[i-3])<int(f[i]):
        count+=1
print(count)
