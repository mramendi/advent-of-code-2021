brackets = { "(":")","[":"]","{":"}","<":">"}
values = { ")":3, "]":57, "}":1197, ">":25137}
values2 = { ")":1, "]":2, "}":3, ">":4}

f = open("input10.txt").readlines()
score=0
scores2=[]
for s in f:
    stack=[]
    valid=True
    for c in s.strip():
        if c in brackets:
            stack.append(brackets[c])
        else:
            if c != stack.pop():
                score+=values[c]
                valid=False
                break
    if valid:
        score2cur=0
        while len(stack)>0:
            score2cur=score2cur*5 + values2[stack.pop()]
        scores2.append(score2cur)

print(score)

scores2.sort()


print(scores2[round((len(scores2)-1)/2)])
