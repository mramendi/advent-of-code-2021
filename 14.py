all_characters=set()
insertions={}
f=open("input14.txt").readlines()
polymer=f[0].strip()
for i in range(2,len(f)):
    if f[i].strip()=="":
        continue
    pair=f[i][0:2]
    insert=f[i][6]
    all_characters.add(pair[0])
    all_characters.add(pair[1])
    all_characters.add(insert)
    insertions[pair]=insert

for cycle in range(40):
    new_polymer=polymer[0]
    for i in range(1,len(polymer)):
        try:
            new_polymer+=insertions[polymer[i-1:i+1]]
        except KeyError:
            pass
        new_polymer+=polymer[i]
    polymer=new_polymer
    print(cycle)

freq={}
for c in all_characters:
    freq[c]=0
for p in polymer:
    freq[p]+=1

print (max(freq.values())-min(freq.values()))
