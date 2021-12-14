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

all_pairs=set()
for c1 in all_characters:
    for c2 in all_characters:
        all_pairs.add(c1+c2)

polymer_pairs_template={}
for pair in all_pairs:
    polymer_pairs_template[pair]=0

polymer_characters={}
for c in all_characters:
    polymer_characters[c]=0

polymer_pairs=polymer_pairs_template.copy()
polymer_characters[polymer[0]]=1
for i in range(1,len(polymer)):
    polymer_characters[polymer[i]]+=1
    polymer_pairs[polymer[i-1:i+1]]+=1

for cycle in range(40):
    new_polymer_pairs=polymer_pairs_template.copy()
    for pair in all_pairs:
        if pair in insertions:
            pair_first=pair[0]+insertions[pair]
            pair_second=insertions[pair]+pair[1]
            new_polymer_pairs[pair_first]+=polymer_pairs[pair]
            new_polymer_pairs[pair_second]+=polymer_pairs[pair]
            polymer_characters[insertions[pair]]+=polymer_pairs[pair]
        else:
            new_polymer_pairs[pair]+=polymer_pairs[pair]
    polymer_pairs = new_polymer_pairs

print (max(polymer_characters.values())-min(polymer_characters.values()))
