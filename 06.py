f = open("input6.txt").readlines()
fish = [int(x) for x in f[0].split(",")]
for i in range(80):
    print(i)
    new_fish=0
    for j in range(len(fish)):
        if fish[j]==0:
            new_fish+=1
            fish[j]=6
        else:
            fish[j]-=1
    fish+=[8]*new_fish
print(len(fish))
