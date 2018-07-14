import unittest


def bfs_get_path(graph, start_node, end_node):
    # Find the shortest route in the network between the two users
    vstd = []
    prnt = {}
    queue = []
    flag = False
    strt = graph.setdefault(start_node, None)
    end = graph.setdefault(end_node, None)
    if(strt == None or end == None):
        raise Exception
    queue.append(start_node)
    while(len(queue)>0 and flag == False):
        node = queue.pop(0)
        if(node not in vstd):
            vstd.append(node)
            temp = graph[node]
            for x in temp:
                if (x!=end_node and x not in vstd):
                    prnt[x]=node
                    queue.append(x)
                elif(x==end_node):
                    queue.append(x)
                    prnt[x]=node
                    flag = True
                    break
    val = prnt.setdefault(end_node,None)
    
    if (val == None):
        return None
    else:
        res = []
        current = end_node
        while(current != start_node):
            res.append(current)
            current = prnt[current]
        res.append(current)
        res.reverse()
        return res
 

