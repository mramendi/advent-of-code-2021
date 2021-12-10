import statistics
f = open("input7.txt").readlines()
positions = [int(x) for x in f[0].split(",")]

# precalculate cost of steps
steps=[0]
for i in range(1,1500):
    steps.append(steps[i-1]+i)

final_fuel=99000000

aim_approx=round(statistics.mean(positions))

for aim in range(aim_approx-5, aim_approx+5):
    fuel=0
    for position in positions:
        fuel+=steps[abs(position-aim)]
    if fuel<final_fuel:
        final_fuel = fuel

print(final_fuel)
