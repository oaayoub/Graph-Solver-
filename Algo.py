import queue
import Graph

def DFS(graph, S, G, visited=[], path=[]):
    print(S)
    if S not in graph:
        print("ERROR NOT IN GRAPH")
    path.append(S)
    if S == G:
        # print("FOUNDS")
        # print(path,"Path")
        return path

    if S not in visited:
        visited.append(S)
        # print(S)
        if S in graph:
            for i in graph[S]:
                # print(i,"Children")
                if DFS(graph, i, G, visited, path):
                    # print(path, "Path")
                    return path
    if path:
        path.pop()
    return False


def BFS(graph, S, G, Queue=[], visited=[], path=[]):
    queue = [(S, [S])]
    visited = set()

    while queue:
        s, path = queue.pop(0)
        visited.add(s)
        if s in graph:
            for node in graph[s]:
                if node == G:
                    return path + [G]
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))


def Limited_DFS(graph, S, G, li, lv, visited=[], path=[]):
    print("limited dfs started", li, " ", lv)
    path.append(S)
    print(S)
    if lv <= li:
        print("INSIDE")
        if S not in graph:
            print("ERROR NOT IN GRAPH")
        if S == G:
            # print("FOUNDS")
            # print(path,"Path")
            return path

        if S not in visited:
            visited.append(S)
            # print(S)
            if S in graph:
                for i in graph[S]:
                    # print(i,"Children")
                    if Limited_DFS(graph, i, G, li, lv + 1, visited, path):
                        # print(path, "Path")
                        print("limited dfs working")
                        return path
    if path:
        path.pop()
    return False


def Itr_Lim_DFS(graph, S, G, max_depth, step):
    counter = step
    print("HERE")
    while counter <= max_depth:
        print(counter)
        if Limited_DFS(graph, S, G, counter, 0, visited=[], path=[]):
            return Limited_DFS(graph, S, G, counter, 0, visited=[], path=[])
        counter = counter + step
'''
def Uniform_Cost_search(graph,S,G,visited=[],path=[]):
    graph.makeDS()
    dist = graph.vertix_list
    nV=graph.number_verticies
    for i in dist:
        dist[i]=1e7
        print(dist)
    dist[S]=0
    PQ = []
    for i in range (V):
        u = -1
        for j in graph.vertix_list:
'''






'''
gEX = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}
# graph, S, G,limit,level=0,visited=[],path=[]
print(Limited_DFS(gEX, '1', '6', 2, 0, visited=[], path=[]))
print(DFS(gEX, '1', '6', visited=[], path=[]))
'''
