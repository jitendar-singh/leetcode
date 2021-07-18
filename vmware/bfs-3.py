from queue import Queue

adj_list = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A","E","F"],
    "E": ["D","F","G"],
    "F": ["D","E","H"],
    "G": ["E","H"],
    "H": ["G","F"]
}

parent, level, visited, output, queue = {}, {}, {}, [], Queue()

'''
Initialization
'''
for node in adj_list.keys():
    parent[node] = None
    level[node] = -1
    visited[node] = False

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)
# output.append(s)

while not queue.empty():
    u = queue.get()
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v]= level[u]+1
            output.append(v)
            queue.put(v)
print(output)






# print(parent)
# print(level)
# print(visited)



