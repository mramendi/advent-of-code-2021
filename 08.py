# letters as a list, for ease of looping
letters=list("abcdefg")


f = open("input8.txt").readlines()

number_unique=0
for s in f:
    [unique, current] = s.strip().split("|")
    curr_list=current.split()
    for outp in curr_list:
        if len(outp) in [2,3,4,7]:
            number_unique+=1
print(number_unique)

sum_total=0

#TEMP
#f=["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

for s in f:
    print(s)
    [unique_line, current_line] = s.strip().split("|")
    uniques = ["".join(sorted(x)) for x in unique_line.split()]
    presence = {}
    translate = {}
    digits = [" "]*10
    for letter in letters:
        count=0
        for unique in uniques:
            if letter in unique:
                count+=1
        presence[letter] = count
    print(presence)
    for letter,pres in presence.items():
        if pres==9:
            translate["f"]=letter
        if pres==6:
            translate["b"]=letter
        if pres==4:
            translate["e"]=letter
    for unique in uniques:
        if len(unique)==2:
            digits[1] = unique
        if len(unique)==3:
            digits[7] = unique
        if len(unique)==4:
            digits[4] = unique
        if len(unique)==7:
            digits[8] = unique
    for chr in digits[1]:
        if chr != translate["f"]:
            translate["c"] = chr
            break
    for chr in digits[7]:
        if not chr in [translate["f"],translate["c"]]:
            translate["a"] = chr
            break
    for chr in digits[4]:
        if not chr in [translate["b"],translate["c"],translate["f"]]:
            translate["d"] = chr
            break
    for chr in letters:
        if not chr in translate.values():
            translate["g"] = chr
            break


    print(translate)

    transl = "".maketrans(translate)

    print ("a".translate(transl))
    print ("abcefg".translate(transl))

    digits[0]="".join(sorted("abcefg".translate(transl)))
    digits[2]="".join(sorted("acdeg".translate(transl)))
    digits[3]="".join(sorted("acdfg".translate(transl)))
    digits[5]="".join(sorted("abdfg".translate(transl)))
    digits[6]="".join(sorted("abdefg".translate(transl)))
    digits[9]="".join(sorted("abcdfg".translate(transl)))

    #interpret the display
    print(uniques)
    print(digits)
    currents = ["".join(sorted(x)) for x in current_line.split()]
    dispnum=0
    for i in range(4):
        dispnum = dispnum*10 + digits.index(currents[i]) # shift the previous digits left
    sum_total += dispnum

print (sum_total)
