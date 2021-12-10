# BRUTE FORCE every board has every column and row as a set
f = open("input4.txt").readlines()

i=2
board_lists=[]
board_setlists=[]
while i<len(f):
    board_list=[]
    board_setlist=[]
    # read lines, save as lists AND sets
    while (i<len(f) and f[i].strip()!=""):
        s=f[i].strip()
#        print (s)
        line=[int(x) for x in s.split()]
#        print(line)
        board_list.append(line)
        board_setlist.append(set(line))
        i+=1
    # save columns as sets only

    for j in range(0,len(board_list[0])):
        column=set()
        for line in board_list:
            column.add(line[j])
        board_setlist.append(column)
    # save board
    board_lists.append(board_list)
    board_setlists.append(board_setlist)
    i+=1

# now is the time to call out numbers
numbers=[int(x) for x in f[0].split(",")]
number_index=0
number_set_so_far=set()
winning_board_index=-1
while number_index<len(numbers): # not using a for loop as we will need the number_index value
    number_set_so_far.add(numbers[number_index])
    for board_index in range(0,len(board_setlists)):
        board_setlist = board_setlists[board_index]
        for board_set in board_setlist:
            if board_set.issubset(number_set_so_far):
                winning_board_index = board_index
        if winning_board_index>-1:
            break
    if winning_board_index>-1:
        break
    number_index+=1

if winning_board_index==-1:
    print("Winning board not found")
    exit(1)

# calculate sum of numbers NOT "called out"
board_list=board_lists[winning_board_index]
sum=0
for line in board_list:
    for n in line:
        if not (n in number_set_so_far):
            sum+=n

print (sum*numbers[number_index])
