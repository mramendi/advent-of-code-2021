version_sum = 0
def parse_packet(packet,depth):
    '''parse a binary packet
    packet is a string representation of binary
    (because I can handle strings better :) )
    returns a tuple (version,type,content,rest)
    version is the version, as an int (also added to version_sum)
    type is the type, as an int
    content: if type is 4, then content is the number as an int
      otherwise content is a list of contents of sub-packets
    rest: the part iof the input string that remains after one packet was parsed
    '''
    global version_sum

    # if the packet is all zeros, it's the padding
    if packet.find("1")==-1:
        print("zeros dropped")
        return(0,0,[],"")

    if depth==0:
        print(packet)

    s_version=packet[0:3]
    s_type=packet[3:6]
    s_rest=packet[6:]

    version=int(s_version,2)
    type=int(s_type,2)

    version_sum+=version

    if type==4:
        s_literal=""
        while s_rest:
            s_literal+=s_rest[1:5]
            q=s_rest[0]
            s_rest=s_rest[5:]
            if q=="0":
                break
        return (version,type,int(s_literal,2),s_rest)
    else:
        if s_rest[0]=="0":
            leng=int(s_rest[1:16],2)
            s_rest=s_rest[16:]
            s_subpackets=s_rest[:leng]
            s_rest=s_rest[leng:]
            print("Length-based start:",leng,"at depth:",depth)
            content=[]
            while s_subpackets:
                print("Length-based ongoing:",len(s_subpackets),"at depth:",depth)
                t_version,t_type,t_content,s_subpackets=parse_packet(s_subpackets,depth+1)
                content.append(t_content)
            print("Length-based completed at depth:",depth)
            return (version,type,content,s_rest)
        else:
            num=int(s_rest[1:12],2)
            print("Number-based start:",num,"at depth:",depth)
            s_rest=s_rest[12:]
            content=[]
            aa=list(range(num))
            for i in aa:
                print("Number-based:",i,"at depth:",depth)
                #print(s_rest)
                t_version,t_type,t_content,s_rest=parse_packet(s_rest,depth+1)
                content.append(t_content)
            return (version,type,content,s_rest)


f = open("input16.txt").readlines()
top_packet=bin(int(f[0],16))[2:].zfill(len(f[0])*4)
parse_packet(top_packet,0)
print(version_sum)

# Testing infrastructure for short examples - comment out the above, uncomment this
#test_str="A0016C880162017C3686B18A3D4780"
#top_packet=bin(int(test_str,16))[2:].zfill(len(test_str)*4)
#print (parse_packet(top_packet,0))
#print(version_sum)
