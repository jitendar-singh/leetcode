from queue import Queue
# from collections import Counters
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

for nodes in adj_list.keys():
    parent[nodes] = None
    visited[nodes] = False
    level[nodes] = -1

root = "A"
visited[root] = True
level[root] = 0
queue.put(root)

while not queue.empty():
    u = queue.get()
    visited[u] = True
    output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
print(output)
            
path = []
destination = "G"

while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(path)
