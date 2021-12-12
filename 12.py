def how_many_paths_to_end(start_node,paths,no_go,exception_used,path_string):
    '''
    recursive walk

    Parameters:
    start_node (string) - the node from which we walk
    paths (dict) - a dictionary where every node has a set of connected nodes
    no_go (set) - a set of nodes that can not be visited as they are "small caves" and were visited; an exception can be used to visit one small cave twice
    exception_used (boolean): if True, the exception for visiting a small cave
      twice was already used; for part 1 answer set to True from the start
    '''

    new_path_string=path_string+" "+start_node

    if start_node == "end":
        # print(new_path_string) # UNCOMMENT TO PRINT PATHS
        return 1 # there is exactly one path from end to end

    new_no_go = no_go.copy()
    if start_node[0].islower():
        new_no_go.add(start_node) # small caves can only be visited once

    count = 0

    for connected_node in paths[start_node]:
        new_exception_used=exception_used
        if connected_node=="start":
            continue
        if connected_node in no_go:
            if exception_used:
                continue
            new_exception_used=True
        if start_node[0].isupper() and connected_node[0].isupper():
            print("WARNING: path between two large caves, infinite loop likely: "+start_node+","+connected_node)
        count += how_many_paths_to_end(connected_node,paths,new_no_go,new_exception_used,new_path_string)
    return count

paths = {}
for s in open("input12.txt"):
    if s.strip()=="": continue
    p1,p2=s.split("-")
    p1=p1.strip()
    p2=p2.strip()
    if not p1 in paths:
        paths[p1]=set()
    if not p2 in paths:
        paths[p2]=set()
    paths[p1].add(p2)
    paths[p2].add(p1)
print("Part 1: ",how_many_paths_to_end("start",paths,set(),True,""))
print("Part 2: ",how_many_paths_to_end("start",paths,set(),False,""))
