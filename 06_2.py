# NOTE: this was made with a hint from reddit, the "buckets meme" as it is called there

f = open("input6.txt").readlines()
fish = [int(x) for x in f[0].split(",")]
buckets=[0]*9
for f in fish:
    buckets[f]+=1

for i in range(256):
    new_fish=buckets[0]
    for j in range(8):
        buckets[j]=buckets[j+1]
    buckets[8]=new_fish
    buckets[6]+=new_fish
print(sum(buckets))
