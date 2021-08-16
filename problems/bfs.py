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

visited, parent, level, output, queue = {}, {}, {}, [], Queue()
for nodes in adj_list.keys():
    parent[nodes] = None
    visited[nodes] = False
    level[nodes] = -1
# print(parent)
# print(visited)
# print(level)
s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while(not queue.empty()):
    u = queue.get()
    output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
print(output)
print(level)
print(level["D"])
print(level["G"])

destination = "G"
path = []

while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(path)
